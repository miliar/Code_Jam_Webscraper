#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

unsigned long main() {

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	unsigned long T, n;
	string name;

	cin >> T;
	for (unsigned long i = 0; i < T; i++) {
		cin >> name >> n;
		unsigned long count = 0;

		unsigned long startPos = 0, endPos = n - 1, lastEndPos = 0;
		while (endPos < name.length()) {
			unsigned long pass = true;
			for (unsigned long j = startPos; j <= endPos; j++)
			{
				if (name[j] == 'a' || name[j] == 'e' || name[j] == 'i' || name[j] == 'o' || name[j] == 'u') {
					pass= false;
					break;
				}
			}
			if (!pass) {
				startPos++;
				endPos++;
				continue;
			}

			count += (startPos - lastEndPos + 1)*(name.length() - endPos);
			lastEndPos = startPos + 1;

			startPos++;
			endPos++;
		}
		
		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}