#include<bits/stdc++.h>
using namespace std;
string a;
void reverse(int from,int to)
{
    while(from<=to)
    {
        if(a[from]=='+') a[from]='-';
        else a[from]='+';
        if(from!=to)
        {
            if(a[to]=='+') a[to]='-';
            else a[to]='+';
        }
        swap(a[from],a[to]);
        from++,to--;
    }
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;cin>>T;
	for(int ks=1;ks<=T;ks++)
    {
        cin>>a;
        cout<<"Case #"<<ks<<": ";
        int sa=a.size();
        int ans=0;
        for(int i=sa-1;i>=0;i--)
        {
            if(a[i]=='-')
            {
                int cnt=0;
                while(a[cnt]=='+')  cnt++;
                if(cnt>0)
                {
                    ans++;
                    reverse(0,cnt-1);
                }
                ans++;
                reverse(0,i);
            }
        }
        cout<<ans<<'\n';
    }
	return 0;
}
