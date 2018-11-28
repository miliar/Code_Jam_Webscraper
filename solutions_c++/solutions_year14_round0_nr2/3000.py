#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int test,case_no=0;
    double c,f,x=0;
    double r1,r2=0;
    double a1,a2=0;
    double div1,div2=0;
    double res=0;
    double prev=0,a1_sum=0;
    freopen("b.txt","r",stdin);
    freopen("bout.txt","w",stdout);
    cin>>test;
    case_no=0;
    while(case_no<test)
    {
        case_no++;
        cin>>c>>f>>x;
        r1=r2=a1=a2=0;
        prev=0;
        a1_sum=0;
        div1=2;
        div2=2;
        r1=x/div2;
       // cout<<endl<<case_no<<" : "<<r1<<" "<<r2<<" "<<prev<<" \n";
        while(1)
        {

            div2=div2+f;

            a1=c/div1;
            div1=div1+f;
            a2=x/div2;
            r2=prev+a1+a2;

            prev=prev+a1;
            //cout<<endl<<case_no<<" : "<<div1<<" "<<div2<<" "<<a1<<" "<<a2<<" "<<r1<<" "<<r2<<" "<<prev<<" \n";
            if (r1>r2)
            {
                r1=r2;
            }

            else if(r1<=r2)
            {
                res=r1;
                goto result ;

            }



        }
        result:
        //cout<<"Case #"<<case_no<<": "<<res<<endl;
        printf("Case #%d: %.6f\n",case_no,res);

    }



}
