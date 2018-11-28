// normal_distribution
#include <iostream>
#include <random>
#include <fstream>
using namespace std;



class Matrix {
public:
  Matrix(unsigned rows, unsigned cols);
  int& operator() (unsigned row, unsigned col);
  int  operator() (unsigned row, unsigned col) const;
   ~Matrix();                              // Destructor
  Matrix(Matrix const& m);               // Copy constructor
  Matrix& operator= (Matrix const& m);   // Assignment operator

private:
  unsigned rows_, cols_;
  int* data_;
};

inline
Matrix::Matrix(unsigned rows, unsigned cols)
  : rows_ (rows)
  , cols_ (cols)
  //data_ <--initialized below (after the 'if/throw' statement)
{
  //if (rows == 0 || cols == 0)
    //throw BadIndex("Matrix constructor has 0 size");
  data_ = new int[rows * cols];
}

inline
Matrix::~Matrix()
{
  delete[] data_;
}

inline
int& Matrix::operator() (unsigned row, unsigned col)
{
  //if (row >= rows_ || col >= cols_)
    //throw BadIndex("Matrix subscript out of bounds");
  return data_[cols_*row + col];
}

inline
int Matrix::operator() (unsigned row, unsigned col) const
{
  //if (row >= rows_ || col >= cols_)
    //throw BadIndex("const Matrix subscript out of bounds");
  return data_[cols_*row + col];
}


int main(){
    ifstream in("B-large.in");
    ofstream cout("output.txt");
    //istream& in=cin;
    int T;
    int N,M;
    in>>T;
    for(int t=0;t<T;t++){
        in>>N>>M;
        Matrix mat(N,M);
        bool ans = true;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                in>>mat(i,j);
            }
        }

        // start checking
        int* rowmax = new int[N];
        int* colmax = new int[M];
        for(int i=0;i<N;i++){
            rowmax[i] = 0;
            for(int j=0;j<M;j++){
                if(mat(i,j)>rowmax[i])
                    rowmax[i] = mat(i,j);
            }
        }
        for(int j=0;j<M;j++){
            colmax[j] = 0;
            for(int i=0;i<N;i++){
                if(mat(i,j)>colmax[j])
                    colmax[j] = mat(i,j);
            }
        }

        //test
//        for(int j=0;j<M;j++){
//            cout<<colmax[j];
//        }
//        for(int j=0;j<N;j++){
//            cout<<rowmax[j];
//        }

        for(int i=0;i<N;i++)
            for(int j=0;j<M;j++){
                if(mat(i,j)<colmax[j]&&mat(i,j)<rowmax[i]){
                    ans=false;
                    break;
                }
            if(!ans)
                break;
            }

        cout<<"Case #"<<t+1<<": ";
        if(ans)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
        }
//        for(int i=0;i<N;i++){
//            for(int j=0;j<M;j++)
//                cout<<mat(i,j);
//            cout<<endl;
//        }

    return 0;
}
