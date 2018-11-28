#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>

typedef std::vector<int> audience;
std::vector<audience> cases;
int n_cases;

std::vector<int> results;

int solve(audience au, int casen);

int main()
{
	//input
	std::ifstream input;
	input.open("input_large.in");
	if(!input.eof())
	{
		input>>n_cases;
		for(int i = 0; i < n_cases; i++)
		{
			audience this_case;
			int n_people;
			std::string this_audience;
			
			input>>n_people;
			input>>this_audience;
			
			std::cout<<n_people<<" "<<this_audience<<std::endl;
			
			for(int j = 0; j <= n_people; j++)
			{
				this_case.push_back(this_audience[j] - 48);
				std::cout<<this_case[j];
			}
			std::cout<<std::endl;
			
			cases.push_back(this_case);
		}
	}
	input.close();
	
	//check if input is correct
	/*
	std::ofstream checkinput;
	checkinput.open("checkinput.txt");
	checkinput<<"Number of cases: "<<cases.size()<<std::endl;
	for(int i = 0; i < cases.size(); i++)
	{
		checkinput << "Case #" << i+1 << ": ";
		checkinput << cases[i].size() << " ";
		for(int j = 0; j < cases[i].size(); j++) checkinput<<cases[i][j];
		checkinput<<std::endl;
	}
	*/
	
	//solve
	for(int i = 0; i < cases.size(); i++) results.push_back(solve(cases[i], i));
	
	//print output
	std::ofstream output;
	output.open("output_large.txt");
	for(int i = 0; i < results.size(); i++)
	{
		output<<"Case #"<<i+1<<": "<<results[i]<<std::endl;
	}
	output.close();
}

int solve(audience au, int casen)
{
	std::ofstream ckout;
	std::stringstream sstm;
	sstm << "checkoutput " << casen << "_large.txt";
	ckout.open(sstm.str().c_str());
	
	int friends = 0;

	ckout<<"Case. Audience size: "<<au.size()<<"."<<std::endl;
	ckout<<"People with no shyness: "<<au[0]<<std::endl;
		
	for(int i = 1; i < au.size(); i++)
	{
	 	ckout<<"People with "<<i<<" shyness: "<<au[i]<<" - ";
		
		int standing = friends;
		for(int j = 0; j < i; j++) standing+=au[j];
		
		int friends_to_call = i - standing;
		if(standing < i) friends += friends_to_call;

		ckout<<"People already standing: "<<standing<<", required: "<<i<<". We need to call "<<friends_to_call<<" more friends."<<std::endl;
	}
	
	ckout.close();
	
	return friends;
}

