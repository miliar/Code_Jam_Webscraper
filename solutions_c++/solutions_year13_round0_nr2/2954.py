#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool checkVertical(int *mat,int i,int j,int N,int M)
{
    int x=*(mat+(i*M)+j);
    int *ptr;
    
    ptr=(mat+j);
    for(int a=0;a<N;a++)
    {
        if((*ptr)>x)
        {
            return false;
        }
        ptr+=M;
    }
    return true;
}

bool checkHorizontal(int *mat,int i,int j,int N,int M)
{
    int x=*(mat+((i*M)+j));
    int *ptr=NULL;
    
    ptr=(mat+(i*M));
    for(int a=0;a<M;a++)
    {
        if(*ptr>x)
        {
//            cout << "x:" << x << " v:" << *ptr << " a:" << a << endl;
            return false;
        }
        ptr++;
    }
    return true;
}

int main ()
{
    vector<int> data;
    ifstream infile ("/Users/diego/Desktop/Google Code Jam/lawnmower/data.in");
    ofstream outFile ("/Users/diego/Desktop/Google Code Jam/lawnmower/data.out");
    
    int cases,N,M;
    
    if (infile.is_open() && outFile.is_open())
    {
        infile >> cases;
        for(int i=0;i<cases;i++)
        {
            infile >> N;
            infile >> M;
            int mat[N][M];
            
            //read
            for(int a=0;a<N;a++)
            {
                for(int b=0;b<M;b++)
                {
                    infile >> mat[a][b];
//                    cout << mat[a][b] << "\t";
                }
//                cout << endl;
            }
            
            //process
            try
            {
                for(int a=0;a<N;a++)
                {
                    for(int b=0;b<M;b++)
                    {
                        if(!checkHorizontal(&mat[0][0], a, b, N, M))
                        {
                            if(!checkVertical(&mat[0][0], a, b, N, M))
                            {
                                throw 1;
                            }
                        }
                    }
                }
                outFile << "Case #" << i+1 << ": YES" << endl;
            }
            catch(int e)
            {
//                cout << "Case #" << i+1 << ": NO" << endl;
                outFile << "Case #" << i+1 << ": NO" << endl;
            }
        }
        
        infile.close();
        outFile.close();
    }
    else cout << "Unable to open file";
    
    return 0;
}