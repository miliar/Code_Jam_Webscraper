#include <iostream>
#include <fstream>
#include <iomanip>
typedef long long lint;
using namespace std;

int  main()
{
    lint test,count=0;
    ifstream myfile;
    ofstream ans;
    double cost,fast,required,speed=2.0,totaltime=0.0,curt,upt;
    ans.open("ans.txt");
    myfile.open("A-small-attempt0.in");
    if (myfile.is_open())
      {
       myfile>>test;
       while(test--)
       {
           cout<<"\ntest"<<test<<"\n";
           myfile>>cost>>fast>>required;
           totaltime=0.0;
           speed=2.0;
           //cout<<cost<<endl<<fast<<endl<<required<<endl;
           while(1){
            upt=(cost/speed)+(required/(speed+fast));
            curt=(required/speed);
            if(curt<upt)
            {
                cout<<cost<<endl<<fast<<endl<<required<<endl;
               totaltime=totaltime+(required/speed);
               cout<<totaltime<<" if "<<endl;
               break;
            }
            else
            {
                totaltime+=cost/speed;
                cout<<totaltime<<" else "<<endl;
                speed+=fast;
            }
           }
           count++;







            ans<<"Case #"<<count<<": "<<std::fixed << std::setprecision(7)<<totaltime<< "\n";


       }

      }

    myfile.close();
    ans.close();

    return 0;
}
