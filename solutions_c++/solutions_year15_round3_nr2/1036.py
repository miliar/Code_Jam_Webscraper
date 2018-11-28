#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int k,l,s,bananas,space,big;
string keys,y;
int match(string &x)
{
    int i,j,z,c=0;
    for(i=0;i<y.size();i++)
    {
        for(j=i,z=0;z<l;z++,j++)
            if(x[z]!=y[j])
                break;
        if(z==l)
            c++;
    }
    return c;
}
void rec(int ind,string &x)
{
    if(ind==s)
    {
        int temp=match(x);
        if(temp>big)
            big=temp;
        bananas+=temp;
        space++;
        return;
    }
    int i;
    for(i=0;i<keys.size();i++)
    {
        y+=keys[i];
        rec(ind+1,x);
        y.erase(y.end()-1);
    }
}
int main()
{
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\out.txt","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        int i;
        space=big=bananas=0;
        y="";
        string x;
        cin>>k>>l>>s>>keys>>x;
        rec(0,x);
        double ans=big;
        ans-=double(bananas)/space;
        cout<<"Case #"<<cas++<<": ";
        printf("%.6lf\n",ans);
    }

    return 0;
}
