#include <iostream>
#include <vector>

using namespace std;
bool isPalindrome(int n) 
{
	char buffer[256];
	sprintf(buffer, "%d", n);
	char revstr[256];
	strcpy(revstr, buffer);
	strrev(revstr);
	return strcmp(revstr, buffer) == 0;
}

int main(int argc, char ** argv) 
{
	// build the numbers
	unsigned char f_num_map[1002];
	unsigned char fs_num_map[1002]; 
	int fs_num_count[1002]; // ith index is count of f&s numbers upto i

	memset(f_num_map, 0, sizeof(fs_num_map));
	memset(fs_num_map, 0, sizeof(fs_num_map));
	memset(fs_num_count, 0, sizeof(fs_num_count));
	
	f_num_map[1] = 1;
	fs_num_map[1] = 1;
	fs_num_count[1] = 1;
	for(int i = 2; i * i <= 1000; i++) {
		if(!f_num_map[i] && isPalindrome(i)) {
			f_num_map[i] = 1;
			int j = i;
			while((j *= j) <= 1000) {
				if(isPalindrome(j)) {
					f_num_map[j] = 1;
					fs_num_map[j] = 1;
				} else break;
			}
		}
	}

	for(int i = 2; i <= 1000; i++) {
		fs_num_count[i] = fs_num_count[i - 1] + fs_num_map[i];
	}

	//cout << "count : " << fs_num_count[1000] << endl;
	int T;
	cin >> T;

	for(int tcase = 1; tcase <= T; tcase++) {
		int A, B;
		cin >> A >> B;
		cout << "Case #" << tcase << ": " << (fs_num_count[B] - fs_num_count[A-1]) << endl;
	}
	return 0;
}