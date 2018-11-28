#include <iostream>
#include <string>
#define INF 32767

using namespace std;

class P{
public:
int	no;
char	c;
	
	P(){
		no = 0;
		c = '\0';
	}
	
};

int main(){
int	T, i;
	cin >> T;
	for(i = 0 ; i < T ; i++){
	int	N, j, k, total = 0;
		cin >> N;
	P	arr[N];
		for(j = 0 ; j < N ; j++){
			cin >> arr[j].no;
			arr[j].c = char(j + 65);
			total += arr[j].no;
		}
		cout << "Case #" << i + 1 << ": ";
		while(total != 0){
		int	max = arr[0].no, maxi = 0, max1 = -INF, max1i = -1;
			for(j = 1 ; j < N ; j++){
				if(arr[j].no > max){
					max1 = max;
					max1i = maxi;
					max = arr[j].no;
					maxi = j;
				}
				else if(arr[j].no <= max && arr[j].no > max1){
					max1 = arr[j].no;
					max1i = j;
				}
			}
			if(max > max1 || total - 2 == 1){
				cout << char(maxi + 65) << ' ';
				arr[maxi].no--;
				total--;
			}
			else if(max == max1){
				cout << char(maxi + 65) << char(max1i + 65) << ' ';
				arr[maxi].no--;
				arr[max1i].no--;
				total -= 2;
			}
		}
		cout << endl;
	}
	return 0;
}
