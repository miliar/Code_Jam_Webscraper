#include <iostream>
#include <fstream>
using namespace std;
int t,m[10],a[26];
void check_0()
{
  if(a[25]!=0){  m[0]=a[25];
    a[4]-=a[25];
    a[17]-=a[25];
    a[14]-=a[25];
    a[25]=0;
  }
}
void check_2()
{
    if(a[22]!=0)
    {
    m[2]=a[22];
    a[19]-=a[22];
    a[14]-=a[22];
    a[22]=0;
    }
}
void check_4()
{

    if(a[20]!=0)
    {

        m[4]=a[20];
        a[14]-=a[20];
        a[5]-=a[20];
         a[17]-=a[20];
        a[20]=0;    }
}
void check_6()
{

 if(a[23]!=0)
 {
     m[6]=a[23];
     a[8]-=a[23];
     a[18]-=a[23];
    a[23]=0;
 }
}
void check_8()
{
    if(a[6]!=0)
    {
        m[8]=a[6];
        a[4]-=a[6];
        a[8]-=a[6];
        a[7]-=a[6];
        a[19]-=a[6];
        a[6]=0;
    }

}
void check_1()
{
    if(a[14]!=0)
    {
        m[1]=a[14];
        a[13]-=a[14];
        a[4]-=a[14];
        a[14]=0;
    }

}
void check_3()
{
    if(a[17]!=0)
    {
        m[3]=a[17];
        a[19]-=a[17];
        a[7]-=a[17];
        a[4]-=a[17]*2;
    a[17]=0;
    }
}
void check_5()
{
 if(a[5]!=0)
 {
     m[5]=a[5];
     a[8]-=a[5];
     a[21]-=a[5];
     a[4]-=a[5];
    a[5]=0;

 }
}
void check_7()
{
    if(a[18]!=0)
    {
        m[7]=a[18];
        a[4]-=a[18]*2;
        a[21]-=a[18];
        a[13]-=a[18];
    a[18]=0;
    }

}
void check_9()
{
    if(a[8]!=0)
    {
        m[9]=a[8];
    }
}
int main()
{
    //cout << "Hello world!" << endl;
    int i,j,k,y;
    char s[2001];
    fstream f2,f1;
    f2.open("input.txt",ios::in);
    f1.open("output.txt",ios::out);
    cin>>t;
    //f2>>t;
    y=1;
    while(y<=t)
    {
        cin>>s;
      //  f2>>s;
        for(i=0;i<26;i++)
            a[i]=0;
        for(i=0;i<10;i++)
            m[i]=0;
        for(i=0;s[i]!='\0';i++)
        {
            k = (int)s[i];
            k-=65;
            a[k]++;
        }
        check_0();
        check_2();
        check_4();
        check_6();
        check_8();
        check_1();
        check_3();
        check_5();
        check_7();
        check_9();
       cout<<"Case #"<<i<<": ";
      //  f1<<"Case #"<<y<<": ";
        for(i=0;i<10;i++)
        {
            for(j=0;j<m[i];j++)
              cout<<i;
          //      f1<<i;
        }
        cout<<"\n";
        //f1<<"\n";
        y++;
    }
    return 0;
}
