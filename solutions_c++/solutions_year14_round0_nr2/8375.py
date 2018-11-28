#include <iostream>
#include <fstream>
#include <string>
#include <sstream>


using namespace std;


int main()
{
    string line;
    int case_total;
    
    double c=0,f=0,x=0;
    double time=0,time1=0,f1=2;
    double m[3];
    
    ifstream myfile ("Input.txt");
    ofstream outfile ("Output.txt");
    outfile.is_open();
    if (myfile.is_open())
    {
     getline (myfile,line);
     case_total = atoi( line.c_str());
     //cout<<case_total<<endl;
     for(int i=0;i<case_total;i++)
     {
             f1=2;
             outfile<<"Case #"<<i+1<<": ";
             cout<<"Case #"<<i+1<<": ";
             
                     getline (myfile,line);
             
                     stringstream stream(line);
                     
                     for(int l=0;l<3;l++)
                     {
                     double n;
                     stream>>n;
                     m[l]=n;
                    
                     }
     
             
     
                     for(int l=0;l<3;l++)
                               {
                                          cout<<m[l]<<" ";
                                }        
                    cout<<endl;
                    
                    c=m[0];
                    f=m[1];
                    x=m[2];
                   
                    time=x/f1;
                   // cout<<"x"<<x<<endl;
                    //cout<<"f1"<<f1<<endl;
                    //cout<<"time: "<<time<<endl;
                    time1=c/f1;
                    //cout<<"time1: "<<time1<<endl;
                    f1=f1+f;
                    time1=time1+x/f1;
                    //cout<<"time1: "<<time1<<endl;
                    while(time1<time)
                    {
                    time=time1;
                    //cout<<"time: "<<time<<endl;
                    time1=time1-x/f1;
                    //cout<<"time1: "<<time1<<endl;
                    time1=time1+c/f1;
                    //cout<<"time1: "<<time1<<endl;
                    f1=f1+f;
                    time1=time1+x/f1;
                    //cout<<"time1: "<<time1<<endl;
                    }
                    cout.precision(9);
                    outfile.precision(9);
                    cout<<"timelast: "<<time<<endl;
                    outfile<<time<<endl;
   
   
}
//             outfile<<"Volunteer cheated!"<<endl;
                   
          myfile.close();
          outfile.close();   
     }

  else cout << "Unable to open file"; 

    system("pause");
    return 0;
}
