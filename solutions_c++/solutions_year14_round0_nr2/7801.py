#include <iostream>
#include <fstream>
using namespace std;
#include <iomanip>
int main()
{
	
/*	int ans1, ans2;
    int a[4][4],b[4][4];
    int x[4],y[4]; */
    
    int dummy;

    ifstream inFile;
    ofstream outFile;
    char inputFilename[] = "B-small-attempt0.in";
    //char inputFilename[] = "A-small2.in";
    char outputFilename[] = "B-small-output.out";
    
    inFile.open(inputFilename, ios::in);
    
    if (!inFile) {
       cout << "Can't open input file " << inputFilename << endl;
       //exit(1);
    }

    outFile.open(outputFilename, ios::out);

    if (!outFile) {
       cout << "Can't open output file " << outputFilename << endl;
      // exit(1);
    }
    
   
   	int T;
   	inFile>>T ; 
	double C,F,X;
    
    //cin>>T;
	for(int i=0;i<T;i++)
    {
        double presentRate = 2;
        double accumTime = 0;
        bool cont = true;
		//cin>>C>>F>>X;
		inFile>>C>>F>>X;
		
		while (cont)
		{
            //cout<<"accum time "<<accumTime<<endl;
            double presTime = (X/presentRate);
    		double newRate = presentRate + F;
    		double newTime = C/presentRate + X/newRate;
    		if (newTime < presTime)
    		{
                 accumTime += C/presentRate;
                 presentRate = newRate;
            }
            else
            {
                // stop the loop
                cont = false;
                accumTime += presTime;
            }     
        }
        //cout<<"Case #"<<i+1<<": "<<setprecision(30)<<accumTime<<endl;
        outFile<<"Case #"<<i+1<<": "<<setprecision(30)<<accumTime<<endl;
    }
    cin.get();
    cin.ignore();
    return 0;
}



