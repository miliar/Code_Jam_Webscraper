#include <iostream>

#include <fstream>
#include <string>

using namespace std;


void main()
{
	ifstream in("A-large.in");
//	streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	cin.rdbuf(in.rdbuf());//redirect std::cin to in.txt!

	ofstream out("A-large.out");
//    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf());

	int testcase;
	cin>>testcase;

	for(int i = 0; i< testcase ; i++)
	{

		int maxshylvl;
		cin>>maxshylvl;
		string x;
		int *shyness = new int[maxshylvl+1];
		int *sum = new int[maxshylvl+1];
		cin>>x;
		for(int j = 0 ; j<=maxshylvl;j++)
		{
			shyness[j]=x[j]-'0';
			sum[j] = 0;
			if(j == 0)
			{
				sum[j] = shyness[j];
			}
			else
				sum[j] = shyness[j]+sum[j-1];
		}
		int countneeded= 0 ;
		for(int s = 1;s<=maxshylvl;s++)
		{
			if(shyness[s]!=0 && s>sum[s-1]+countneeded)
			{
				int k = s-sum[s-1]-countneeded;
				countneeded+= k;
				
			}
		}
		//cout<<"Max "<<maxshylvl<<" " <<x<<" ";
		cout<<"Case #"<<i+1<<": "<<countneeded<<endl;
	}

}