#include<bits/stdc++.h>

using namespace std;

int main(){
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int p=1;p<=t;p++){
        int n;
        cin >> n;
        if(n==0){
            cout << "Case #" << p <<": INSOMNIA" << endl;
        }
        else{
            int a[10] = {0};
            //fill_n(a,a+10,0);
            int j = 1;
            int sum = 0;
            int k;
            while(sum<10){
                k = j*n;
                ostringstream convert;
                string s;
                convert << k;
                s = convert.str();
                //cout << s << endl;
                int l = s.length();
                for(int j=0;j<l;j++){
                    if(a[s[j]-48]==0){
                        a[s[j]-48] = 1;
                        sum++;
                    }
                }
                j++;
            }
            cout << "Case #" << p << ": " << k << endl;

        }
    }

    return 0;
}
