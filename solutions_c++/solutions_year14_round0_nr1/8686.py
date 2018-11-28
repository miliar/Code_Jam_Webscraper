#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int T, N, M;
    fin >> T;
    
    int input1[4][4];
    int input2[4][4];

    for (int t = 1 ; t <= T; t++)
    {  
        fin >> N;
		for (int i = 0 ; i < 4 ; i++)
			for (int j = 0 ; j < 4 ; j++)
				fin >> input1[i][j];

        fin >> M;
		for (int i = 0 ; i < 4 ; i++)
			for (int j = 0 ; j < 4 ; j++)
				fin >> input2[i][j];		

       int found = 0;
       int answer = 0;
       for (int i = 0 ; i < 4 ; i++) {
           bool f = false;
           for (int j = 0 ; j < 4 ; j++)           
               if (input1[N-1][i] == input2[M-1][j])
                  {answer = input1[N-1][i]; f = true; break;}
           if (f) found ++; 
       }
       
       fout << "Case #" << t << ": ";
       if (found > 1)
          fout << "Bad magician!" << endl;
       else if (found == 0)
            fout << "Volunteer cheated!" << endl;
       else
           fout << answer << endl;       
    }
}
