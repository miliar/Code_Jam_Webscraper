#include <bits/stdc++.h>
using namespace std;

bool bot(string ar){
    for(int i=0;i<ar.size();i++){
        if(ar[i]=='-')return false;

    }
    return true;
}


int main(){
freopen("D:\\B-large.in","r",stdin);
freopen("D:\\outputFileName.txt","w",stdout);
	int t;
	cin>>t;
	string j;
	getline(cin,j);
	for(int i=1;i<=t;i++){
        string s;
        getline(cin,s);

        int c=0;
        while(true){
            bool a=bot(s);
            if(a)break;
            char t=s[0];
            char u;
            if(t=='+')u='-';
            else u='+';
            for(int x=0;x<s.size();x++){
                if(s[x]==t){
                    s[x]=u;
                }else{

                 break;
                }
            }
            c++;
        }
        printf("Case #%d: %d\n",i,c);

	}
}
