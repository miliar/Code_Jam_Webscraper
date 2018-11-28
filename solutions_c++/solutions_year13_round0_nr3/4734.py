#include <iostream>
#include <stdio.h>
using namespace std;

//str1>str2 or not
int isGreat(string str1,string str2)
{
    int siz_str1=str1.size(),siz_str2=str2.size();
    if(siz_str1<siz_str2)
        return 0;
    else if(siz_str1>siz_str2)
        return 1;
    else
    {
        for(int j=0;j<siz_str1;j++)
        {
            if(str1[j]>str2[j])
                return 1;
            else if(str1[j]<str2[j])
                return 0;
        }

    }
    return 2;
}

int main()
{
    int test;
    string a[]={"1","4","9","121","484","10201","12321","14641","40804",
                 "44944","1002001","1234321","4008004","100020001","102030201",
                 "104060401","121242121","123454321","125686521","400080004","404090404",
                 "10000200001","10221412201","12102420121","12345654321","40000800004","1000002000001",
                 "1002003002001","1004006004001","1020304030201","1022325232201","1024348434201",
                 "1210024200121","1212225222121","1214428244121","1232346432321","1234567654321",
                 "4000008000004","4004009004004"};
    int siz=39;
    //int a[]={1,4,9,121,484};
    scanf("%d",&test);
    int k=0;
    while(k<test)
    {
        string A,B;
        cin>>A>>B;
//        int siz_A=A.size();
//        int siz_B=B.size();
        int count=0;
        if(k>0)
            cout<<"\n";

//        cout<<A<<B<<"\n";
        //for(;(a[i]<A) &&(i<5) ;i++);
        int i=0;
        while(i<siz)
        {
            int res=isGreat(a[i],A);
//            cout<<res<<"\n";
            if(res==0)
                i++;
            else
                break;
        }
//cout<<"2nd loop"<<"\n";
        while(i<siz)
        {
            int res=isGreat(a[i],B);
//            cout<<res<<"\n";
            if(res==1)
                break;
            else
                count++;
            i++;
        }
        cout<<"Case #"<<k+1<<": "<<count;
        k++;
    }
    return 0;
}
