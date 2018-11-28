#include<iostream>
#include<fstream>
#include<list>
using namespace std;
int main()
{
    list<char> strings;
    string str;
    int i,n,j,t;
    char c;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d",&t);
    list<char>::iterator p=strings.begin();
    for(i=1;i<=t;i++)
    {
        cin>>str;//printf("Beginning case %d\n",i);
        n=str.size();
        for(j=0;j<n;j++)
        {
            c=str[j];
            p=strings.begin();
            if(c<*p)
            strings.push_back(c);
            else
            strings.push_front(c);
        }
        printf("Case #%d: ",i);
        p=strings.begin();
        while(p!=strings.end()){cout<<*p;p++;}
        printf("\n");
        strings.clear();
    }
    return 0;
}
