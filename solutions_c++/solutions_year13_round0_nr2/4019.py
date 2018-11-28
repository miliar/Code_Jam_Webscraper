#include <iostream>
#include <string>

using std::cout;
using std::cin;
 
int N, M;
bool res;
int lawn[110][110];
 
 
bool checkPattern (int pattern, int x, int y)
{
        int checkCol = 0;
		int checkRow = 0;
        for(int column = 0 ; column < M ; column++)
        {
                if(lawn[x][column] <= pattern) 
				{
					checkCol++;
				}
                else 
				{
					break;
				}
        }
 
        for(int row = 0 ; row < N ; row++)
        {
                if(lawn[row][y] <= pattern) 
				{
					checkRow++;
				}
                else 
				{
					break;
				}
        }
 
        if(checkCol == M || checkRow == N) 
		{
			return true;
		}
        else 
		{
			return false;
		}
 
}
 
int main()
{
       int test, count = 1;
       cin >> test;
       while(test--)
       {
               cin >> N >> M;
 
               for(int i = 0 ; i < N ; i++)
               {
                       for(int j = 0 ; j < M ; j++)
                       {
                               cin >> lawn[i][j];
                       }
               }
 
               res = true;
 
               for(int i = 0 ; i < N ; i++)
               {
                       for(int j = 0 ; j < M ; j++)
                       {
                               int pattern = lawn[i][j];
                               res = checkPattern(pattern, i, j);
                               if(!res)
								{
									break;
								}
                        }
                        if(!res) break;
                }
 
                printf("Case #%d: ", count++);
                if(res)
				{
					cout << "YES\n";
				}
                else 
				{
					cout << "NO\n";
				}
        }
        return 0;
}