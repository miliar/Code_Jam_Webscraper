#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int main()
{
    ifstream fin("D-large.in");
    ofstream fout("D-large.out");
    int T,N;
    float Naomi[1000];
    float Ken[1000];
    char Order1[2000];
    char Order2[2000];
    
    fin >> T;
    cout <<T<<endl;
    for (int t=0;t<T;t++ )
    {
        fin >> N;
        for (int i=0;i<N;i++)
        {
            fin >> Naomi[i];
        }
        for (int i=0;i<N;i++)
        {
            fin >> Ken[i];
        }
        // Rank two arrays; 
        float tmp;
        for (int i=0;i<N-1;i++)
            for (int j=i+1;j<N;j++)
            {
                if( Naomi[i]> Naomi[j] )
                {
                    tmp = Naomi[i];
                    Naomi[i] = Naomi[j];
                    Naomi[j] = tmp;
                }
            }        
        for (int i=0;i<N-1;i++)
            for (int j=i+1;j<N;j++)
            {
                if( Ken[i]> Ken[j] )
                {
                    tmp = Ken[i];
                    Ken[i] = Ken[j];
                    Ken[j] = tmp;
                }
            }
        // Merge into one rows;
        int p,q,i;
        p = 0;
        q = 0;
        i = 0;
        while(i < 2*N)
        {
            if (p == N)
            {
               Order1[i] = Order2[i]=  'K' ;
               q = q+1;
               i = i+1;
               continue;
            }
            if (q == N)
            {
               Order1[i] = Order2[i]=  'N' ;
               p = p+1;
               i = i+1;
               continue;
            }
            if( Naomi[p] < Ken[q] )
            {
               Order1[i] = Order2[i]=  'N' ;
               p = p+1;
            }
            else
            {
               Order1[i] = Order2[i]=  'K' ;
               q = q+1;                
            }
            i = i+1;
        }
                
        // 
        int Score_War = 0;
        for (int k=0;k<N;k++)
        {
            int p=0;
            while ( Order1[p]!='N' )
                p = p+1;
            int q=p+1;
            while ( Order1[q]!='K' && q< 2*N )
                q = q+1;
            if (q == 2*N)
            {
                q = 0;
                while ( Order1[q]!='K' )
                    q = q+1;
                Score_War = Score_War+1;
            }
            Order1[p] = Order1[q] = 'F';
        }        
        
        //
        int Score_Deceitful = 0;
        int k;
        for (k=0;k<N;k++)
        {
            int p=0;
            while ( Order2[p]=='F' )
                p = p+1;
                
            if ( Order2[p]=='N' )
            {
                int q=2*N-1;
                while ( Order2[q]!='K'  )
                    q = q-1;
                Order2[p] = Order2[q] = 'F';
            }
            else // Order2[p]=='K'
            {
                int q=p+1;                
                while ( Order2[q]!='N'  )
                    q = q+1;
                Order2[p] = Order2[q] = 'F';
                Score_Deceitful = Score_Deceitful+1;
            }
        }        
        
        fout << "Case #" << t+1 << ": " << Score_Deceitful << " " << Score_War << endl;

    }     
    fin.close();
    fout.close();
    
    return 0;
}
