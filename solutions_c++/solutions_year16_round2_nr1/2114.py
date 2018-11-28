#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;cin>>T;
	for(int ks=1;ks<=T;ks++)
    {
        int cnt[30];
        string a;cin>>a;
        memset(cnt,0,sizeof(cnt));
        int sa=a.size();
        for(int i=0;i<sa;i++) cnt[(int)(a[i]-'A')]++;
        int ans[10];
        memset(ans,0,sizeof(ans));
        if(cnt[(int)('Z'-'A')]>0)
        {
            ans[0]+=cnt[(int)('Z'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('Z'-'A')];
            cnt[(int)('R'-'A')]-=cnt[(int)('Z'-'A')];
            cnt[(int)('O'-'A')]-=cnt[(int)('Z'-'A')];
            cnt[(int)('Z'-'A')]-=cnt[(int)('Z'-'A')];
        }
        if(cnt[(int)('W'-'A')]>0)
        {
            ans[2]+=cnt[(int)('W'-'A')];
            cnt[(int)('T'-'A')]-=cnt[(int)('W'-'A')];
            cnt[(int)('O'-'A')]-=cnt[(int)('W'-'A')];
            cnt[(int)('W'-'A')]-=cnt[(int)('W'-'A')];
        }
        if(cnt[(int)('X'-'A')]>0)
        {
            ans[6]+=cnt[(int)('X'-'A')];
            cnt[(int)('S'-'A')]-=cnt[(int)('X'-'A')];
            cnt[(int)('I'-'A')]-=cnt[(int)('X'-'A')];
            cnt[(int)('X'-'A')]-=cnt[(int)('X'-'A')];
        }
        if(cnt[(int)('G'-'A')]>0)
        {
            ans[8]+=cnt[(int)('G'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('G'-'A')];
            cnt[(int)('I'-'A')]-=cnt[(int)('G'-'A')];
            cnt[(int)('H'-'A')]-=cnt[(int)('G'-'A')];
            cnt[(int)('T'-'A')]-=cnt[(int)('G'-'A')];
            cnt[(int)('G'-'A')]-=cnt[(int)('G'-'A')];
        }
        if(cnt[(int)('H'-'A')]>0)
        {
            ans[3]+=cnt[(int)('H'-'A')];
            cnt[(int)('T'-'A')]-=cnt[(int)('H'-'A')];
            cnt[(int)('R'-'A')]-=cnt[(int)('H'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('H'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('H'-'A')];
            cnt[(int)('H'-'A')]-=cnt[(int)('H'-'A')];
        }
        if(cnt[(int)('R'-'A')]>0)
        {
            ans[4]+=cnt[(int)('R'-'A')];
            cnt[(int)('F'-'A')]-=cnt[(int)('R'-'A')];
            cnt[(int)('U'-'A')]-=cnt[(int)('R'-'A')];
            cnt[(int)('O'-'A')]-=cnt[(int)('R'-'A')];
            cnt[(int)('R'-'A')]-=cnt[(int)('R'-'A')];
        }
        if(cnt[(int)('O'-'A')]>0)
        {
            ans[1]+=cnt[(int)('O'-'A')];
            cnt[(int)('N'-'A')]-=cnt[(int)('O'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('O'-'A')];
            cnt[(int)('O'-'A')]-=cnt[(int)('O'-'A')];
        }
        if(cnt[(int)('S'-'A')]>0)
        {
            ans[7]+=cnt[(int)('S'-'A')];
            cnt[(int)('V'-'A')]-=cnt[(int)('S'-'A')];
            cnt[(int)('N'-'A')]-=cnt[(int)('S'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('S'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('S'-'A')];
            cnt[(int)('S'-'A')]-=cnt[(int)('S'-'A')];
        }
        if(cnt[(int)('F'-'A')]>0)
        {
            ans[5]+=cnt[(int)('F'-'A')];
            cnt[(int)('I'-'A')]-=cnt[(int)('F'-'A')];
            cnt[(int)('V'-'A')]-=cnt[(int)('F'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('F'-'A')];
            cnt[(int)('F'-'A')]-=cnt[(int)('F'-'A')];
        }
        if(cnt[(int)('I'-'A')]>0)
        {
            ans[9]+=cnt[(int)('I'-'A')];
            cnt[(int)('N'-'A')]-=cnt[(int)('I'-'A')];
            cnt[(int)('N'-'A')]-=cnt[(int)('I'-'A')];
            cnt[(int)('E'-'A')]-=cnt[(int)('I'-'A')];
            cnt[(int)('I'-'A')]-=cnt[(int)('I'-'A')];
        }
        cout<<"Case #"<<ks<<": ";
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<ans[i];j++) cout<<i;
        }
        cout<<'\n';
    }
	return 0;
}
