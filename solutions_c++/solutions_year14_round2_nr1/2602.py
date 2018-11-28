#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

int brute(string s1,string s2){
    //cout<<s1<<" "<<s2<<endl;
    int j = 0;
    int i = 0;
    int ans = 0;
    while(true)
    {
        int f1 = 1;
        while(i+1<s1.length() && s1[i]==s1[i+1]){i++;f1++;}
        int f2 = 1;
        while(j+1<s2.length() && s2[j]==s2[j+1]){j++;f2++;}

        if(s1[i]!=s2[j])return -1;
        ans += abs(f2-f1);
        i++;
        j++;
        if(i==s1.length())break;
        if(j==s2.length())break;
    }
    if(i!=s1.length())return -1;
    if(j!=s2.length())return -1;
    return ans;
}

int main(int argc, char const *argv[])
{
    int T,N;
    string str;
    cin>>T;
    for (int t = 0; t < T; ++t){
        cin>>N;
        vector<int> freq[100]; 
        char cs[100];
        bool ans = true;
        string st[2];
        int finalcont = 0;
        for (int n = 0; n < N; ++n)
        {
            cin>>str;
            st[n&1] = str;
            int ind = 0;
            int cont = 0;
            while(ind<str.length()){
                int f = 1;
                while(ind+1<str.length() && str[ind]==str[ind+1]){
                    ind++;
                    f++;
                }
                if(n==0){
                    cs[cont] = str[ind];
                    freq[n].push_back(f);
                }
                else{
                    if(str[ind]!=cs[cont]){
                        ans = false;
                        break;
                    }
                    else{
                        freq[n].push_back(f);
                    }
                }
                ind++;
                cont++;
            }
            if(n==0)finalcont = cont;
            if(finalcont != cont) ans = false;
            if(!ans)break;
        }
        cout<<"Case #"<<t+1<<": ";
        if(!ans){
            cout<<"Fegla Won"<<endl;
            continue;
        }
        int final = 0;
        for (int i = 0; i < freq[0].size(); ++i)
        {
            int cost;
            int tmp = 100000000;
            for(int pos = 1 ; pos <= 100; pos++){
                cost = 0;
                for(int n=0; n < N;n++){
                    //if(pos==1)cout<<freq[n][i]<<" debug "<<n<<" "<<i<<endl;
                    cost += abs(pos-freq[n][i]);
                }
                //cout<<cost<<" "<<pos<<endl;
                tmp = min(tmp,cost);
            }
            final += tmp;
        }
        cout<<final<<endl;
    }
    return 0;
}