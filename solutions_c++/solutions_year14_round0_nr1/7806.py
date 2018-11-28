#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    
	int T;
	int ans1, ans2;
    int a[4][4],b[4][4];
    int x[4],y[4];
    
    int dummy;

    ifstream inFile;
    ofstream outFile;
    char inputFilename[] = "A-small-attempt1.in";
    //char inputFilename[] = "A-small2.in";
    char outputFilename[] = "A-small-output.out";
    
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
    
    
   inFile >> T ;
    
    //cout<<T;
	for(int i=0;i<T;i++)
    {
        // input first answer    
		//cin>>ans1;
		inFile>>ans1;
		
		//input first array
		for(int j=0;j<4;j++)
		{
            for(int k=0; k<4; k++)
            {
               //cin>>a[j][k];
               inFile>>a[j][k];
            }
		}
		
	    // input second answer    
		//cin>>ans2;
		inFile>>ans2;
		
		//input second array
		for(int j=0;j<4;j++)
		{
            for(int k=0; k<4; k++)
            {
               //cin>>b[j][k];
               inFile>>b[j][k];
            }
		}
		
		int aRow = ans1 - 1;
		int bRow = ans2 - 1;
		
		int resultCount = 0;
		int result = 0;
		
		
        for(int j=0;j<4;j++)
		{
            for(int k=0; k<4; k++)
            {
               if (a[aRow][j] == b[bRow][k])
               {
                   resultCount = resultCount + 1;
                   result = a[aRow][j];
               }
            }
		}
		if (resultCount == 1)
		{
             //cout<<"Case #"<<i+1<<": "<<result<<endl;
             outFile<<"Case #"<<i+1<<": "<<result<<endl;
        }
        else if (resultCount == 0)
        {
             //cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
             outFile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
        else
        {
            //cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
             outFile<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
    }
    cin.get();
    cin.ignore();
    return 0;
}



