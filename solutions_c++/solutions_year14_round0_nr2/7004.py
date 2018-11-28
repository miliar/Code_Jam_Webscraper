#include<iostream>
#include<fstream>
#include<sstream>
#include<iomanip>
using namespace std;
int main()
{
    ifstream afile("B-large.in",ios::in);
    ofstream myfile("outputcoke.txt");
    string sample;
    int total,i=0,ctr=0;
    double c,f,x,rate=2.0000000,t2,t1,totalt=0.0000000;

    getline(afile,sample);
    stringstream conv;
    conv<<sample;
    conv>>total;
    while(i<total)
    {
        rate=2.0000000;
        totalt=0.0000000;
        getline(afile,sample);
        conv.str("");
        conv.clear();
        conv<<sample;
        conv>>c;
        conv>>f;
        conv>>x;
        cout<<c<<"\t";
        while(1)
        {

            t2=c/rate;
            t1=x/rate;
            totalt+=t2;
            //cout<<fixed<<t1<<"  "<<fixed<<t2<<"  ";
            if(t1<c/rate+x/(rate+f))
            {
                //cout<<"exit";
                break;
            }
            rate=rate+f;
        };
        myfile<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<totalt+t1-t2<<endl;
        i++;
        //cout<<fixed<<c<<" "<<fixed<<f<<" "<<fixed<<x<<endl;
    }
}
