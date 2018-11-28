#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int T;
    cin >> T;
    int t = 1;
    while(T--){
        string x;
        cin >> x;
        int ans = 0;
        bool curr = false;
        reverse(x.begin(),x.end());
        for(int i=0;i<x.size();i++){
            if(x[i] == '+')continue;
            ans++;
            int j ;
            for(j=x.size()-1;j>i;j--){
                if(x[j] == '+')continue;
                break;
            }
            if(j != (int)x.size()-1 && j >= i){
				j++;
				ans++, reverse(x.begin()+j,x.end());
				for(j ; j<x.size();j++){
					if(x[j] == '+')x[j] = '-';
					else x[j] = '+';
				}
			}
            reverse(x.begin()+i,x.end());
            for(int j=i ; j<x.size();j++){
				if(x[j] == '+')x[j] = '-';
				else x[j] = '+';
			}
        }
        cout << "Case #"<<t++<<": ";
        cout << ans << endl;
    }
    return 0;
}
