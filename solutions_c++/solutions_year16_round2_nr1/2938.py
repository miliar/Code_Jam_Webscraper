#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;
string num[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX", "SEVEN", "EIGNT", "NINE"};
   int cnt[26];
   int result[10];

void reduce(char c,int x)
{
    result[x]+=cnt[c-'A'];
//    cout<<x<<' '<<result[x]<<' '<<c<<endl;
    string str = num[x];
//    cout<<str<<endl;
    for(int j=0;j<str.size();j++)
        cnt[str[j]-'A']-= result[x];
}
int main()
{
//    freopen("input.txt","r",stdin);
 //   freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    string str;
    string feature;
    feature = "ZWUXGOTFSI";
    int order[] = {0,2,4,6,8,1,3,5,7,9};
   for(int t=1;t<=T;t++){
        cin>> str;
        memset(cnt,0,sizeof(cnt));
        memset(result,0,sizeof(result));
        for(int i=0;i<str.size();i++)
            cnt[str[i]-'A']++;
        for(int i=0;i<10;i++)
            reduce(feature[i],order[i]);
        cout<<"Case #"<<t<<": ";
        for(int i=0;i<10;i++)
            for(int j=0;j<result[i];j++)
                cout<<i;
        cout<<endl;
   }
   
   return 0;
}

