#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>
#include <sstream>
#include <fstream>
#include <ctime>

using namespace std;

class TicTac
{
public:

    TicTac() :
        m_infileName(""),
        m_outfileName(""),
        m_T(0)
    {
        ClearVariableState();
        InitResultSet();
    }

    TicTac( string infileName, string outfileName ) :
        m_infileName(infileName),
        m_outfileName(outfileName),
        m_T(0)
    {
        ClearVariableState();
        InitResultSet();
    }

    ~TicTac()
    {
    }

    void setInfile( string infileName )
    {
        m_infileName = infileName;
        ClearVariableState();
    }

    void setOutfile( string outfileName )
    {
        m_outfileName = outfileName;
        ClearVariableState();
    }

    void ParseFileAndProcessAlgorithm()
    {
         ifstream inputFile( m_infileName.c_str() );
         ofstream outputFile( m_outfileName.c_str() );

         ClearVariableState();

         string line;
         getline( inputFile, line );
         stringstream sstr(line);
         sstr >> m_T;

         // DumpState();

         bool noDots = true;
         for ( unsigned int i = 0; i < m_T; i++ )
         {
             noDots = true;
             m_XSet.clear();
             m_YSet.clear();

             string gameArray;
             gameArray.clear();
             getline( inputFile, line );
             gameArray += line;
             getline( inputFile, line );
             gameArray += line;
             getline( inputFile, line );
             gameArray += line;
             getline( inputFile, line );
             gameArray += line;
             getline( inputFile, line );

             for ( unsigned j = 0; j < gameArray.size(); j++ )
             {
                 switch ( gameArray[j] )
                 {
                 case 'X':
                     m_XSet.insert( j + 1 );
                     break;
                 case 'O':
                     m_YSet.insert( j + 1 );
                     break;
                 case 'T':
                     m_XSet.insert( j + 1 );
                     m_YSet.insert( j + 1 );
                     break;
                 case '.':
                     noDots = false;
                     break;
                 }
             }

             bool pathFound = false;
             for ( auto it = m_SolutionSets.begin(); (it != m_SolutionSets.end()) && !pathFound; it++ )
             {
                 unsigned XCount = 0;
                 unsigned YCount = 0;
                 for ( auto x : (*it) )
                 {
                     auto xit = m_XSet.find( x );
                     if ( xit != m_XSet.end() )
                     {
                         XCount++;
                     }
                 }

                 if ( XCount == 4 )
                 {
                     pathFound = true;
                     outputFile << "Case #" << i + 1 << ": " << m_resultStrings[0] << endl;
                 }
                 else
                 {
                     for ( auto o : (*it) )
                     {
                         auto yit = m_YSet.find( o );
                         if ( yit != m_YSet.end() )
                         {
                             YCount++;
                         }
                     }

                     if ( YCount == 4 )
                     {
                         pathFound = true;
                         outputFile << "Case #" << i + 1 << ": " << m_resultStrings[1] << endl;
                     }
                 }

                 XCount = 0;
                 YCount = 0;
             }

             if ( !pathFound )
             {
                 if ( noDots )
                 {
                     outputFile << "Case #" << i + 1 << ": " << m_resultStrings[2] << endl;
                 }
                 else
                 {
                     outputFile << "Case #" << i + 1 << ": " << m_resultStrings[3] << endl;
                 }
             }

             // DumpStaticState();
         }
    }

private:

    string m_infileName;
    string m_outfileName;

    unsigned m_T;

    unordered_set< unsigned > m_XSet;
    unordered_set< unsigned > m_YSet;

    vector< unordered_set< unsigned > > m_SolutionSets;
    vector< string > m_resultStrings;

    void InitResultSet()
    {
        m_resultStrings.clear();
        m_resultStrings.push_back( "X won" );
        m_resultStrings.push_back( "O won" );
        m_resultStrings.push_back( "Draw" );
        m_resultStrings.push_back( "Game has not completed" );

        m_SolutionSets.clear();
        unordered_set< unsigned > newSet;

        newSet.clear();
        newSet.insert( 1 );
        newSet.insert( 2 );
        newSet.insert( 3 );
        newSet.insert( 4 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 5 );
        newSet.insert( 6 );
        newSet.insert( 7 );
        newSet.insert( 8 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 9 );
        newSet.insert( 10 );
        newSet.insert( 11 );
        newSet.insert( 12 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 13 );
        newSet.insert( 14 );
        newSet.insert( 15 );
        newSet.insert( 16 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 1 );
        newSet.insert( 5 );
        newSet.insert( 9 );
        newSet.insert( 13 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 2 );
        newSet.insert( 6 );
        newSet.insert( 10 );
        newSet.insert( 14 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 3 );
        newSet.insert( 7 );
        newSet.insert( 11 );
        newSet.insert( 15 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 4 );
        newSet.insert( 8 );
        newSet.insert( 12 );
        newSet.insert( 16 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 1 );
        newSet.insert( 6 );
        newSet.insert( 11 );
        newSet.insert( 16 );
        m_SolutionSets.push_back( newSet );

        newSet.clear();
        newSet.insert( 4 );
        newSet.insert( 7 );
        newSet.insert( 10 );
        newSet.insert( 13 );
        m_SolutionSets.push_back( newSet );
    }

    void ClearVariableState()
    {
        m_T = 0;
        m_XSet.clear();
        m_YSet.clear();
    }
};

int main(int argc, char *argv[])
{
    string inputFN = ".\\A-small-practice.in";
    string outputFN = ".\\out.txt";

    if ( argc == 2 )
    {
        inputFN = argv[1];
    }
    else if ( argc == 3 )
    {
        inputFN = argv[1];
        outputFN = argv[2];
    }

    TicTac al( inputFN, outputFN );
    al.ParseFileAndProcessAlgorithm();

    return 0;
}
