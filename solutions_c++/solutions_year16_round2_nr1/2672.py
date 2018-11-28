#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main(){
    int T=0,k=1;
    cin >> T;
    while(T--){
        string in,ans;
        cin >> in;
        int in_a[30],add[10];
        memset(in_a,0,sizeof(in_a));
        memset(add,0,sizeof(add));
        for (int a=0;a<(int)in.length();a++){
           in_a[in[a]-'A']++;
        }
        while(in_a[25]>0&&in_a[4]>0&&in_a[17]>0&&in_a[14]>0){
			in_a[25]--;
			in_a[4]--;
			in_a[17]--;
			in_a[14]--;
			add[0]++;
        }
        while(in_a[18]>0&&in_a[8]>0&&in_a[23]>0){
			in_a[18]--;
			in_a[8]--;
			in_a[23]--;
			add[6]++;
        }
        while(in_a[18]>0&&in_a[4]>1&&in_a[21]>0&&in_a[13]>0){
			in_a[18]--;
			in_a[4]-=2;
			in_a[21]--;
			in_a[13]--;
			add[7]++;
        }
        while(in_a[5]>0&&in_a[8]>0&&in_a[21]>0&&in_a[4]>0){
			in_a[5]--;
			in_a[8]--;
			in_a[21]--;
			in_a[4]--;
			add[5]++;
        }
        while(in_a[4]>0&&in_a[8]>0&&in_a[6]>0&&in_a[7]>0&&in_a[19]>0){
			in_a[4]--;
			in_a[8]--;
			in_a[6]--;
			in_a[7]--;
			in_a[19]--;
			add[8]++;
        }
        while(in_a[19]>0&&in_a[22]>0&&in_a[14]>0){
			in_a[19]--;
			in_a[22]--;
			in_a[14]--;
			add[2]++;
        }
        while(in_a[13]>1&&in_a[8]>0&&in_a[4]>0){
			in_a[13]-=2;
			in_a[8]--;
			in_a[4]--;
			add[9]++;
        }
        while(in_a[5]>0&&in_a[14]>0&&in_a[20]>0&&in_a[17]>0){
			in_a[5]--;
			in_a[14]--;
			in_a[20]--;
			in_a[17]--;
			add[4]++;
        }
        while(in_a[19]>0&&in_a[7]>0&&in_a[17]>0&&in_a[4]>1){
			in_a[19]--;
			in_a[7]--;
			in_a[17]--;
			in_a[4]-=2;
			add[3]++;
        }
        while(in_a[14]>0&&in_a[13]>0&&in_a[4]>0){
			in_a[14]--;
			in_a[13]--;
			in_a[4]--;
			add[1]++;
        }

		for(int a=0;a<26;a++){
			if(in_a[a]!=0){
				cout << a << endl;
			}
		}

		for(int a=0;a<10;a++){
			for(int b=0;b<add[a];b++){
				ans=ans+(char)(a+'0');
			}
		}

        cout << "Case #" << k << ": " << ans << endl;
        k++;
    }
    return 0;
}

