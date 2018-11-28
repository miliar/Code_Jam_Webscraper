#include<stdio.h>
#include<conio.h>
#include<iostream>
//class counting
//{
      using namespace std;
      
       int main()
      {
      	
      	freopen("A-large.in","r",stdin);
    	freopen("A-large.out","w",stdout);
        
		int t;
        cin>>t;
        long n[t]={0};
        //String[] key=new String[t];
        long h=0,a=0;
        int z=0,o=0,tw=0,th=0,f=0,fi=0,six=0,se=0,ei=0,ni=0,d,i;
        int zero=0,one=0,two=0,three=0,four=0,five=0,si=0,seven=0,eight=0,nine=0;
        for(i=0;i<t;i++)
        {
        cin>>n[i];
        }
        int count;
        for(i=0;i<t;i++)
        {
            h=n[i];
            count=0;
          
           d=2;
           z=0;o=0;tw=0;th=0;f=0;fi=0;six=0;se=0;ei=0;ni=0;
           zero=0;one=0;two=0;three=0;four=0;five=0;si=0;seven=0;eight=0;nine=0;
             if(n[i]==0)
           cout<<"Case #"<<(1+i)<<": INSOMNIA"<<endl;
           else
           {
            while(count!=10)
        {
        while(h!=0)
        {
            a=h%10;
            if(a==0)
            z++;
            if(a==1)
            o++;
            if(a==2)
            tw++;
            if(a==3)
            th++;
            if(a==4)
            f++;
            if(a==5)
            fi++;
            if(a==6)
            si++;
            if(a==7)
            se++;
            if(a==8)
            ei++;
            if(a==9)
            ni++;
            h=h/10;
        }
        if(z>0)
        zero++;
        if(o>0)
        one++;
        if(tw>0)
        two++;
        if(th>0)
        three++;
        if(f>0)
        four++;
        if(fi>0)
        five++;
        if(si>0)
        six++;
        if(se>0)
        seven++;
        if(ei>0)
        eight++;
        if(ni>0)
        nine++;
        if(zero==1)
        {
            zero=2;
        count++;
    }
        if(one==1)
        {
            one=2;
        count++;
    }
        if(two==1)
        { two=2;
        count++;
    }
        if(three==1)
        { three=2;
        count++;
    }
        if(four==1)
        { four=2;
        count++;
    }
        if(five==1)
        { five=2;
        count++;
    }
        if(six==1)
    { six=2;
        count++;
    }    if(seven==1)
    { seven=2;
        count++;}
        if(eight==1){
            eight=2;
        count++;}
        if(nine==1){
            nine=2;
        count++;}
        h=n[i]*d;
        d++;
    }
    long aq=n[i]*(d-2);
   cout<<"Case #"<<(1+i)<<": "<<aq<<endl;
}
    //    }
        
    }
}
