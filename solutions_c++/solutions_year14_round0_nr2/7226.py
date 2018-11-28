#include<cstdio>
#include<iostream>
#include<algorithm>
#include<iomanip>
 using namespace std;


 int main()
 {
     int t,t1,i=0,j=0,k=0,fcount=0;
double c,f,tc,tx,time,timex,timef,timefx,rate,x;

 freopen("B-large.in", "r", stdin);
freopen("finalL.out", "w", stdout);

 cout<<std::fixed;
      cout<<setprecision(7);
     scanf("%d",&t);
     t1=t;
    double result[t];
    while(t--)
    {
        scanf("%lg",&c);
        //cout<<"c is  "<<c;
        scanf("%lg",&f);
        //cout<<"   f is "<<f<<endl;
        scanf("%lg",&x);
        //cout<<endl<<" x is "<<x;
        tc=c/2;
        tx=x/2;
        rate=2+f;
        timefx=tc+x/rate;
        //printf(" tc is  %f\n",tc);
        if(timefx>tx)
        {
            result[i]=tx;
            ++i;

//cout<<tx<<"  1 time"<<endl;
        }
        else{timefx =-1;
            time=tc;rate=2+f;
            timef=tc;timex=tx;
            while(timefx<timex)
            {
                timex=x/rate;
                timef=c/rate;
//out<<timef<<"  time for "<<j<<endl;
                rate+=f;
                timefx=x/rate+timef;
                //cout<<"time fx  "<<timefx<<endl;
               if(timefx<timex)
                    time+=timef;
               // else{
                  //  time+=timex;
                  //  break;

                  ++j;
                }


time+=timex;
        result[i]=time;
        //time=0;
        ++i;}
        }



j=1;

     for(i=0;i<t1;i++)
     {


      cout<<"Case #"<<j<<": "<<result[i]<<endl;
      ++j;
     }



 }
