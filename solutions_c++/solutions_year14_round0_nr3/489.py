#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;
struct Field
{
   Field(ifstream& in)
   {
      in >> R >> C >> M;
      E = R * C - M;
      bPossible = false;
      for( int i = 0; i < R; i++ )
         m_vField.push_back(vector<char>(C, '*'));
   }

   void CreateField(int Empties)
   {

   }

   void Solve()
   {
      if( E == 1 )
      { 
         m_vField[0][0] = 'c';
         bPossible = true;
      }
      else if( R == 1 )
      {
         m_vField[0][0] = 'c';
         for( int i = 1; i < E; i++ )
         {
            m_vField[0][i] = '.';
         }
         bPossible = true;
      }
      else if( C == 1 )
      {
         m_vField[0][0] = 'c';
         for( int i = 1; i < E; i++ )
         {
            m_vField[i][0] = '.';
         }
         bPossible = true;
      }
      else if( E == 4 )
      {
         if( R >= 2 && C >= 2 )
         {
            m_vField[0][0] = 'c';
            m_vField[0][1] = '.';
            m_vField[1][0] = '.';
            m_vField[1][1] = '.';
            bPossible = true;
         }
      }
      else if( E == 6 )
      {
         if( R >= 2 && C >= 2 )
         {
            m_vField[0][0] = 'c';
            m_vField[0][1] = '.';
            m_vField[1][0] = '.';
            m_vField[1][1] = '.';
            if( R > 2 )
            {
               m_vField[2][0] = '.';
               m_vField[2][1] = '.';
            }
            else
            {
               m_vField[0][2] = '.';
               m_vField[1][2] = '.';
            }
            bPossible = true;
         }
      }
      else if( E >= 8 )
      {
         
         int C1 = 2;
         int R1 = E / C1;
         int Max = max(R,C);
         int Rem = E % C1;
         if( R1 > Max )
         {
            Rem += C1 * (R1 - Max) % Max;
            C1 += C1 * (R1 - Max) / Max;
            R1 = Max;
         }        
         else
         {
            if( Rem == 1 )
            {
               Rem += C1;
               R1--;
               if( C1 + 1 > min (R,C) )
               {
                  return;

               }
            }
         }

         int nEmpty = 0;            
         for( int i = 0; i < C1; i++ )
         {
            for( int j = 0; j < R1; j++ )
            {
               nEmpty++;
               if( nEmpty > E )
                  break;
               if( i == 0 && j == 0 )
               {
                  m_vField[i][j] = 'c';
                  continue;
               }
               if( R < C )
               {
                  m_vField[i][j] = '.';
               }
               else
               {
                  m_vField[j][i] = '.';
               }
            }
            if( nEmpty > E )
               break;
         }
         if( R < C )
         {
            for( int i = 0; i < Rem; i++ )
            {
               m_vField[C1][i] = '.';
            }
            if( Rem == 1 && C1 > 2 )
            {
               m_vField[C1-1][R1-1] = '*';
               m_vField[C1][Rem] = '.';
            }
         }
         else
         {
            for( int i = 0; i < Rem; i++ )
            {
               m_vField[i][C1] = '.';
            }
            if( Rem == 1 && C1 > 2 )
            {
               m_vField[R1-1][C1-1] = '*';
               m_vField[Rem][C1] = '.';
            }
         }
         bPossible = true;
      }
   }

   void PrintOutput(ofstream& of)
   {
      for( size_t i = 0; i < m_vField.size(); i++ )
      {
         for( size_t j = 0; j < m_vField[i].size(); j++ )
         {
            of << m_vField[i][j];
         }
         of << endl;
      }
   }

   vector<vector<char> > m_vField;
   int R, C, M, E;

   int RMax, RMin, CMax, CMin;
   bool bPossible;
};

int main()
{
	//ifstream in("C-small-attempt1.in");
   //ofstream out("C-small-attempt1.out");

	ifstream in("C-large.in");
   ofstream out("C-large.out");
	
	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{		
      Field fld(in);
      fld.Solve();
		out << "Case #" << iCount << ":" << endl;
      if( !fld.bPossible )
         out << "Impossible" << endl;
      else
         fld.PrintOutput(out);
	}
	return 0;
}
