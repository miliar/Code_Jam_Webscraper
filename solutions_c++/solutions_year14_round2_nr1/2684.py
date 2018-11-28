#include <conio.h>
#include <iostream>
#include <cstring>

using namespace std;

int const con=150;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);
    int T;
    cin >> T;
    for (int q=0; q<T; q++)
    {
        //cout << "In Case " << q+1 << endl;
        int N;
        cin >> N;
        //cout << N << endl;
        int where[con];
        char str[con][con];
        
        char temp[1];
        cin.getline(temp,1);
        
        for (int i=0; i<N; i++)
            cin.getline(str[i],con);
        for (int i=0; i<N; i++)
            where[i]=0;
            
        //for (int i=0; i<N; i++,cout << endl)
        //    for (int j=0; j<strlen(str[i]);j++)
        //        cout << str[i][j];
               
        bool lose=false;    
        int min=0;
        char c='!';
        
        //cout << str[1][99] << endl;
        
        //cout << "after c=!" << endl;
        for (int w=0; w<N; w++)
        {
            int ind=1;
        c=str[w][where[w]];
        //cout << "after c=where[" << w << "]" <<  endl << "c=" << c << endl;
        while (c!=0)
        {
              //cout << "ind=" << ind << endl;
              //cout << "for c=" << c << endl;
              if (lose) break;
              int hmanyc[con];
              for (int i=0; i<N; i++)
                  hmanyc[i]=0;
              
              for (int i=0; i<N; i++)
              {
                  if (str[i][where[i]]!=c)
                  {
                     //cout << "Oops! There is no '" << c << "' in str[" << i << "][where[" << i << "]]" << endl;
                     //cout << "where[" << i << "]=" << where[i] << endl;
                     //cout << "str[" << i << "][where[" << i << "]]=" << str[i][where[i]] << endl;
                     lose=true;
                     break;
                  }
                  for (;; where[i]++)
                      if (str[i][where[i]]==c)
                      {
                        // cout << "where[" << i << "]=" << where[i] << endl;
                         //cout << "str[" << i << "][where[" << i << "]]=" << str[i][where[i]] << endl;
                         hmanyc[i]++;
                      }
                      else
                          break;
              }
                          
              if (lose) break;
              
              //for (int i=0; i<N; i++)
              //    cout << hmanyc[i] << endl;
              //cout << endl;
              
              int ave=0;
              for (int i=0; i<N; i++)
                  ave+=hmanyc[i];
              ave=ave/N;
              
              for (int i=0; i<N; i++)
                 if (ave>hmanyc[i])
                    min+=ave-hmanyc[i];
                 else
                     min+=hmanyc[i]-ave;
              c=str[w][where[w]];
              
              ind++;
        }
        }
        if (!lose)
           cout << "Case #" << q+1 << ": " << min << endl;
        else
            cout << "Case #" << q+1 << ": Fegla Won" << endl;
    }
    //getch();
    return 0;
}
        
                  
                          
              
