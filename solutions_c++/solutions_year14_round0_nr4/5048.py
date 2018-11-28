#include <iostream>
#include <fstream>

using namespace std;

void Tri(int n, float * num, int m)
{
    if(n==m-1) return;
    float tmp;
    if(num[n]>num[n+1])
    {
        tmp = num[n];
        num[n] = num[n+1];
        num[n+1] = tmp;
        Tri(0,num,m);
    }
    else Tri(n+1,num,m);
}

int Deceitful_War(float *num1, float *num2, int m)
{
    int i, j = 0, pts = 0;
    for(i=0; i<m; i++)
    {
        //if(num1[i]<num2[j]) Can't be trade safely
        if(num1[i]>num2[j]) {j++; pts++;}
    }
    return pts;
}

int War(float *num1, float *num2, int m)
{
    int i, j, pts = 0;
    // Check if a value is already trade
    bool num[m];
    for(i=0; i<m; i++)
        // At the beginning, no value is trade
        num[i] = false;
    for(i=0; i<m; i++)
    {
        for(j=0; j<m; j++)
        {
            if(num1[i]<num2[j] && !num[j]) {pts++; num[j]=true; break;}
        }
    }
    return m-pts;
}

int main(int argc, char *argv[])
{
    ifstream file_input("D-small-attempt0.in", ios::in);
    ofstream file_output("D-small-attempt0(answer).in", ios::trunc | ios::out);
    if(file_input && file_output)
    {
        int games, test=1, i, j;
        float num1[1000], num2[1000];
        file_input >> games;
        while(test<=games)
        {
            file_input >> j;
            for(i=0; i<j; i++)
                file_input >> num1[i];
            Tri(0,num1,j);
            for(i=0; i<j; i++)
                file_input >> num2[i];
            Tri(0,num2,j);

            file_output << "Case #" << test << ": ";
            file_output << Deceitful_War(num1,num2,j) << " " << War(num1,num2,j);
            file_output << "\n";
            test++;
        }
        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file !" << endl;
    return 0;
}
