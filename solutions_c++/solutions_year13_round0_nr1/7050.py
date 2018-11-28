#include<iostream>
#define x 'X'
#define o 'O'
#define t 'T'

using namespace std;

int main()
{
	int n,q;
	cin>>n;
	q = n;
	cin.ignore(1,'\n');
	while(n--)
	{
	    int flag = 0;
		string a,s,d,f;
		cin>>a>>s>>d>>f;
		for(int i=0;i<4;i++)
		{
			if((a[i]==x||a[i]==t)&&(s[i]==x||s[i]==t)&&(d[i]==x||d[i]==t)&&(f[i]==x||f[i]==t))
                flag = 1;
            else if((a[i]==o||a[i]==t)&&(s[i]==o||s[i]==t)&&(d[i]==o||d[i]==t)&&(f[i]==o||f[i]==t))
                flag = 2;
		}
		int i =0;
		if((a[i]==x||a[i]==t)&&(a[i+1]==x||a[i+1]==t)&&(a[i+2]==x||a[i+2]==t)&&(a[i+3]==x||a[i+3]==t))
            flag = 1;
        else if((s[i]==x||s[i]==t)&&(s[i+1]==x||s[i+1]==t)&&(s[i+2]==x||s[i+2]==t)&&(s[i+3]==x||s[i+3]==t))
            flag = 1;
        else if((d[i]==x||d[i]==t)&&(d[i+1]==x||d[i+1]==t)&&(d[i+2]==x||d[i+2]==t)&&(d[i+3]==x||d[i+3]==t))
            flag = 1;
        else if((f[i]==x||f[i]==t)&&(f[i+1]==x||f[i+1]==t)&&(f[i+2]==x||f[i+2]==t)&&(f[i+3]==x||f[i+3]==t))
            flag = 1;
        else if((a[i]==o||a[i]==t)&&(a[i+1]==o||a[i+1]==t)&&(a[i+2]==o||a[i+2]==t)&&(a[i+3]==o||a[i+3]==t))
            flag = 2;
        else if((s[i]==o||s[i]==t)&&(s[i+1]==o||s[i+1]==t)&&(s[i+2]==o||s[i+2]==t)&&(s[i+3]==o||s[i+3]==t))
            flag = 2;
        else if((d[i]==o||d[i]==t)&&(d[i+1]==o||d[i+1]==t)&&(d[i+2]==o||d[i+2]==t)&&(d[i+3]==o||d[i+3]==t))
            flag = 2;
        else if((f[i]==o||f[i]==t)&&(f[i+1]==o||f[i+1]==t)&&(f[i+2]==o||f[i+2]==t)&&(f[i+3]==o||f[i+3]==t))
            flag = 2;
        else if((a[i]==o||a[i]==t)&&(s[i+1]==o||s[i+1]==t)&&(d[i+2]==o||d[i+2]==t)&&(f[i+3]==o||f[i+3]==t))
            flag = 2;
        else if((a[i]==x||a[i]==t)&&(s[i+1]==x||s[i+1]==t)&&(d[i+2]==x||d[i+2]==t)&&(f[i+3]==x||f[i+3]==t))
            flag = 1;
        else if((f[i]==o||f[i]==t)&&(d[i+1]==o||d[i+1]==t)&&(s[i+2]==o||s[i+2]==t)&&(a[i+3]==o||a[i+3]==t))
            flag = 2;
        else if((f[i]==x||f[i]==t)&&(d[i+1]==x||d[i+1]==t)&&(s[i+2]==x||s[i+2]==t)&&(a[i+3]==x||a[i+3]==t))
            flag = 1;
        if(flag == 0)
        {
            for(int i=0;i<4;i++)
            {
                if(a[i]=='.'||s[i]=='.'||d[i]=='.'||f[i]=='.')
                    flag = 3;

            }
        }
        if(flag == 3)
            cout<<"Case #"<<(q-n)<<": Game has not completed"<<endl;
        else if(flag == 1)
            cout<<"Case #"<<(q-n)<<": X won"<<endl;
        else if(flag == 2)
            cout<<"Case #"<<(q-n)<<": O won"<<endl;
        else
            cout<<"Case #"<<(q-n)<<": Draw"<<endl;

	}

	return 0;

}
