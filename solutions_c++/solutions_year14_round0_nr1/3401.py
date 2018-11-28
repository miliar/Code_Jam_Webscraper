#include <fstream>
std::ifstream fin("A-small-attempt0.in");
std::ofstream fout("output.out");
int T, a1, a2, arr[2][4], num, temp[4];
bool flag1, flag2;
int main()
{
    fin>>T;
    for(int i = 0; i< T; i++)
    {
            flag1 = 0;flag2 = 0;
            fin>>a1;
            for(int j =0; j< 4; j++)
            {
                    for(int k =0; k< 4; k++)
                    {
                            fin>>temp[k];
                    }
                    if(j+1 == a1)
                    {
                           for(int k=0; k< 4; k++) arr[0][k] = temp[k];
                    }
            }
            fin>>a2;
            for(int j =0; j< 4; j++)
            {
                    for(int k =0; k< 4; k++)
                    {
                            fin>>temp[k];
                    }
                    if(j+1 == a2)
                    {
                           for(int k=0; k< 4; k++) arr[1][k] = temp[k];
                    }
            }
            for(int j =0; j< 4; j++)
            {
                    for(int k  =0; k< 4; k++)
                    {
                            if(arr[0][j] == arr[1][k] && flag1 == 0){num = arr[0][j];flag1 = 1;}
                            else if(arr[0][j] == arr[1][k] && flag1 == 1){flag2 = 1;}
                    }
            }
            if(flag1 == 0) fout<<"Case #"<<i+1<<": Volunteer cheated!\n";
            else if(flag2 == 0) fout<<"Case #"<<i+1<<": "<<num<<"\n";
                 else fout<<"Case #"<<i+1<<": Bad magician!\n";
    }
    return 0;
}
