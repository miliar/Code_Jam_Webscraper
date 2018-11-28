#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <Windows.h>

using namespace std;

class FileReader : public ifstream
{
public:
   FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
   int readInt() { int x; *this >> x; return x; }
   vector<int> readInts( int n ) { vector<int> v(n); for ( int i = 0; i < n; i++ ) v[i] = readInt(); return v; }
   string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
   string readString() { string x; *this >> x; return x; }
   vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
   __int64 readInt64() { __int64 x; *this >> x; return x; }
};



class FileWriter : public ofstream
{
public:
   FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
};

string doit( FileReader& fin )
{   
   int M = fin.readInt();
   int N = fin.readInt();
   int maxLinha[M];
   int maxColuna[N];
   int numeros[M][N];
   for ( int i = 0; i < N; i++ )
       maxColuna[i]=0;
   for ( int i = 0; i < M; i++ )
       maxLinha[i]=0;
   fin.readLine();
   for ( int i = 0; i < M; i++ )
   {            
          for ( int j = 0; j < N; j++ ) {
              int nn = fin.readInt();
              if(nn>maxLinha[i]) maxLinha[i]=nn;
              if(nn>maxColuna[j]) maxColuna[j]=nn;                            
              numeros[i][j]=nn;
          }
   fin.readLine(); 
   } 
   for ( int i = 0; i < M; i++ )
   {             
          for ( int j = 0; j < N; j++ ) {
              if(numeros[i][j]<maxLinha[i] && numeros[i][j]<maxColuna[j]) return "NO";
          }
   }   
   
   return "YES";
}

int main()
{
   FileReader fin( "B-large.in" );
   FileWriter fout( "out.txt" );
   int T = fin.readInt();
   fin.readLine();
   for ( int i = 0; i < T; i++ )
   {
      stringstream ss;
      ss << "Case #" << i+1 << ": " << doit( fin ) << endl;
      fout << ss.str().c_str();
      OutputDebugStringA( ss.str().c_str() );
   }
   
   return 0;
}
