#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
//FILE *f = fopen("C:\\Users\\naman\\Downloads\\naman.in", "r");
//FILE *f1 = fopen("C:\\Users\\naman\\Downloads\\new.in", "w");
 char s[1001];
    int sm,count1=0,total=0,n,t,ans[100],k=0;

 ifstream infile;
 infile.open("C:\\Users\\naman\\Downloads\\naman.in");
 infile>>t;
 cout<<t;
    //      fscanf(f,"%d\n",&t);
//cout<<t;
ofstream outfile;
outfile.open("C:\\Users\\naman\\Downloads\\new.in",ios::out | ios::trunc);
    for(int j=0;j<t;j++)
    {
        infile>>sm;
        infile>>s;

        count1=0;
        total=0;
    for(int i=0;i<sm+1;i++)
    {
        if((int(s[i])-48)!=0)
            n=i;
    }
    for(int i=0;i<n;i++)
    {
        count1+=(int(s[i])-48);
        if(count1<i+1)
        {
            total+=((i+1)-count1);
            count1+=((i+1)-count1);

        }

    }
     //ans[k]=total;
     k++;
     outfile<<"Case #"<<k<<": "<<total<<endl;
    // fprintf(f1,"case #%d: %d\n",k,total);
    }

//fclose(f);
//fclose(f1);

return 0;
}

