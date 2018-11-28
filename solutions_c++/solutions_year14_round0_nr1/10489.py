#include <iostream>

using namespace std;

int main(void)
{
    int cnt =1;
	int t;
	cin >> t;
	while(t--) {
        int data[20] = {0,};
        int line,tmp;
        for(int k=0;k<2;k++) {

            cin >> line;
            for(int i=1;i<=4;i++) {
                for(int j=1;j<=4;j++) {
                    cin >> tmp;
                    if(i == line) data[tmp] += 1;
            
                }
            }
        }

        int cnt2 = 0;
        for(int i=1;i<=16;i++) {
            if(data[i] == 2) {
                tmp = i;
                cnt2++;
            }
        }
        cout << "Case #"<< cnt << ": ";
        if(cnt2 == 0){
            cout << "Volunteer cheated!";
        }else if(cnt2 == 1) {
            cout << tmp ;
        }else{
            cout << "Bad magician!";
        }
        cout << endl;

        cnt++;
        
	}
	
}

