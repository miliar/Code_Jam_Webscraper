#include<iostream>
#include<fstream>
using namespace std;

int main()
{


ifstream in;
in.open("a.txt");
ofstream out;
out.open("output.txt");


int test_case;
in>>test_case;
for(int i=1; i<=test_case; i++)
{
    int max_shyness_level=0;
    int shyness_levels=0;
    int shyness_people[10]={0};

    int counter=0, num_people=0;
	in>>max_shyness_level;
	in>>shyness_levels;

	for(int j=max_shyness_level; j>=1; j--)
    {
        shyness_people[j]=shyness_levels%10;
        shyness_levels/=10;
    }
        shyness_people[0]=shyness_levels;


    for(int k=0; k<=max_shyness_level; k++)
    {
        if(counter>=k)
        counter+=shyness_people[k];
        else
        {
            num_people++;
            counter++;
            counter+=shyness_people[k];
        }
    }


	out<<"Case #"<<i<<": "<<num_people<<"\n";


}

}

