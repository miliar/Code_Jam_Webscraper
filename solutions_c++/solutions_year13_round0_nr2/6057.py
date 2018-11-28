#include<iostream>
#include<fstream>


using namespace std;

int main()
{
    
    ifstream fin;
    ofstream fout;
    fin.open("B-small-attempt1.in");
    fout.open("output");
    int cases;
    int rows;
    int cols;
    int **array;
    fin>>cases;
    bool errorR;
    bool errorC;
    for(int i=0;i<cases;i++)
    {
            
            fin>>rows;
            fin>>cols;
            
            // Declaring Dynamic array
            array = new int*[rows];
            
            for(int i=0;i<rows;i++)
                    array[i]= new int[cols];
                    
            // inserting values into the array
            
            for(int i=0;i<rows;i++)
                    for(int j=0;j<cols;j++)
                            fin>>array[i][j];
            /*        
            // printing values
            for(int i=0;i<rows;i++)
            {        for(int j=0;j<cols;j++)
                            cout<<array[i][j];
                     cout<<endl;
            }
            */
            
            for(int i=0;i<rows;i++)
            {
                    errorR = errorC = false;
                    for(int j=0;j<cols;j++)
                            {
                                           // Check rows
                                           for(int k=0;k<cols;k++)
                                                   if(array[i][k]>array[i][j])
                                                                              errorR = true;
                                           // Check cols
                                           if (errorR == true)
                                           {
                                           for(int x=0;x<rows;x++)
                                                   if(array[x][j]>array[i][j])
                                                                              errorC = true;
                                           }
                            }
                            
                            if(errorR && errorC)
                                      break;
            }
            
            if(errorR && errorC)
                      fout<<"Case #"<<i+1<<": NO";
            else
                      fout<<"Case #"<<i+1<<": YES";
                      
            fout<<endl;
            
            delete []array;
    
            
    }
    
    fin.close();
    fout.close();
    system("pause");
    return 0;
}
