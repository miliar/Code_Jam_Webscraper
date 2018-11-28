#include <iostream>
#include <fstream>

using namespace std;

ifstream fin;
ofstream fout;

double Naomi[2000];
double Ken[2000];



int main()
{
    fin.open("D-large.in",ios::in);
    fout.open("output.txt",ios::trunc);
    int cases;
    fin>>cases;
    for (int caseNum=1;caseNum <= cases;caseNum++)
    {
        int number;
        fin>>number;
        for (int i=0;i<number;i++)
            fin>>Naomi[i];
        for (int i=0;i<number;i++)
            fin>>Ken[i];
        //sort Naomi
        for (int i=0;i<number;i++)
        {
            double minWeight = Naomi[i];
            int minBlock = i;
            for (int j=i+1;j<number;j++)
                if (Naomi[j] < minWeight)
            {
                minWeight = Naomi[j];
                minBlock = j;
            }
            if ( i != minBlock)
            {
                Naomi[minBlock] = Naomi[i];
                Naomi[i] = minWeight;
            }
        }
        for (int i=0;i<number;i++)
        {
            double minWeight = Ken[i];
            int minBlock = i;
            for (int j=i+1;j<number;j++)
                if (Ken[j] < minWeight)
            {
                minWeight = Ken[j];
                minBlock = j;
            }
            if ( i != minBlock)
            {
                Ken[minBlock] = Ken[i];
                Ken[i] = minWeight;
            }
        }
        //deceitful war
        int ans1 = 0;
        int head = 0;
        for (int i=0;i<number;i++)
        {
            if (Naomi[i] > Ken[head])
            {
                ans1++;
                head++;
            }
        }
        //war
        int ans2 = number;
        for (int i=0;i<number;i++)
        {
            for (int j = 0; j<number;j++)
                if (Ken[j] > Naomi[i])
                {
                    ans2--;
                    Ken[j]=-1;
                    break;
                }
        }
        fout<<"Case #"<<caseNum<<": ";
        fout<<ans1<<" "<<ans2<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
