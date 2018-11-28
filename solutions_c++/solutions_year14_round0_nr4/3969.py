#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
void bubblesort(float a[],int size)
{
    int flag;
    for(int i=0;i<size;i++)
    {
        flag=0;
        for(int j=0;j<size-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                flag++;
                float t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
        }
        if(flag==0)return;
    }
    return;
}
int main()
{
    fstream f1,f2;
    int t;
    f1.open("CJwar",ios::in);
    f2.open("output",ios::out);
    f1.seekg(0);
    f1>>t;
    int win[50],lost[50];
    for(int i=0;i<t;i++)
    {
        int n;
        f1>>n;
        cout<<".."<<i<<".."<<n<<endl;
        float b1[n],b2[n];
        int l=0,w=0;
        for(int j=0;j<n;j++)
            f1>>b1[j];
        for(int j=0;j<n;j++)
            f1>>b2[j];
                f2<<" ";

        bubblesort(b1,n);
        bubblesort(b2,n);
        int f1=0,r1=n-1,f2=0,r2=n-1;

        /*for(int j=0;j<n;j++)
            cout<<b1[j]<<" ";
            cout<<endl;
        for(int j=0;j<n;j++)
            cout<<b2[j]<<" ";
        cout<<endl;*/
        while(1)
        {
            if(b1[f1]<b2[f2]){   l++;   f1++;  r2--;    }
            else{   w++;   f1++;    f2++;       }
            if(w+l==n)break;
        }
        win[i]=w;
        l=0;
        f1=0;f2=0;r1=n-1;r2=n-1;
        for(int j=r2;j>=f2;j--)
        {
            for(int k=r1;k>=f1;k--)
            {
                if(b2[j]>b1[k]){ r2--;  r1--;   l++;   break;    }
                else {r1--;}
            }
        }
        lost[i]=n-l;
    }
    f2.seekg(0);
    for(int i=0;i<t;i++)
        f2<<"Case #"<<i+1<<": "<<win[i]<<" "<<lost[i]<<endl;
    return 0;
}
