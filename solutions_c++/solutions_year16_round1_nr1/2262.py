#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int flag = 0;
int main()
{
    int i, j, tn, n;
    string in;
    freopen("gcal.in", "r", stdin);
    freopen("gcal.out", "w", stdout);
    scanf("%d",&tn);
    for(int tt = 1;tt<=tn;tt++){
        cin>>in;
        string ret = "";
        for(i=0;i<in.size();i++){
            string nxr = ret + in[i];
            string nxl = in[i] + ret;
            ret = max(nxr, nxl);
        }
        cout<<"Case #"<<tt<<": "<<ret<<endl;
    }
    return 0;
}
