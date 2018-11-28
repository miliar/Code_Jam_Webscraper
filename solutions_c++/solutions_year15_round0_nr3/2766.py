/*Dijkstra*/
#include<iostream>
#include<string>
using namespace std;
int index(char c)
{   if(c=='i')
        return 2;
    else if(c=='j')
        return 3;
    else
        return 4;
}
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("3_small.txt","w",stdout);
    int arr[5][5]={0,0,0,0,0,0,1,2,3,4,0,2,-1,4,-3,0,3,-4,-1,2,0,4,3,-2,-1};
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {   int l,x,x1;
        cin>>l>>x;
        x1=x;
        string s="";
        string temp;
        cin>>temp;
        while(x--)
            s+=temp;
        int a=index(s[0]),i=1,flag=1;
        while(a!=2&&i<l*x1)
        {   if(a<0)
               a=-1*(arr[-a][index(s[i])]);
            else
                a=arr[a][index(s[i])];
            i++;
        }
        int i1,j1;
        i1=i;
        if(i==l*x1)
            flag=0;
        if(flag)
        {   i=l*x1-2;
            a=index(s[l*x1-1]);
            while(i>=0&&a!=4)
            {   if(a<0)
                    a=-1*(arr[index(s[i])][-a]);
                else
                    a=arr[index(s[i])][a];
                i--;
            }
            if(i==-1)
                flag=0;
            j1=i;
        }
        if(i1>j1)
            flag=0;
        if(flag)
        {   a=index(s[i1]);
            i1++;
            while(i1<=j1)
            {   if(a<0)
                    a=-1*(arr[-a][index(s[i1])]);
                else
                    a=arr[a][index(s[i1])];
                i1++;
            }
            if(a!=3)
                flag=0;
        }
        cout<<"Case #"<<cas<<": ";
        if(flag)
            cout<<"YES\n";
        else
            cout<<"NO\n";
        cas++;
    }
    return 0;
}
