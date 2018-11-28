#include<bits/stdc++.h>
using namespace std;

int main()
 {

   freopen("A-small.in.txt","r",stdin);
     freopen("output.txt","w",stdout);
   int tcase;
   cin>>tcase;


   int pl;
   for(pl=1;pl<=tcase;pl++)
     {

       string st;
       cin>>st;

       string opstr="";
       int l=st.size();
       int i;

       char ch;
       for(i=0;i<l;i++)
        {
           ch=s[i];
           if(opstr=="")
             opstr+=ch;
           else if(opstr[0]>ch)
               opstr=opstr+ch;
               else
               opstr=ch+opstr;
        }
        cout<<"Case #"<<pl<<": "<<opstr<<endl;
    }
 }
