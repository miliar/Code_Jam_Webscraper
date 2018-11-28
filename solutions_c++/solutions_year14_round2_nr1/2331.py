#include<iostream>
#include<cstring>

using namespace std;


int main()
{
	string str[100];
	int numTestCases;
	int count = 0;
	int N;
	cin>>numTestCases;
	
	for(int i = 0; i < numTestCases; i++){
		count = 0; 
		cin>>N;
		
		
		for(int  j = 0; j < N; j++){
			cin>>str[j];
		}
		
		if(str[0].at(0) != str[1].at(0)){
				count = -1;
				cout<<"Case #"<<(i+1)<<": Fegla Won\n";
				continue;
		}
		else{
		
			for(int k = 1; k < str[0].length() || k < str[1].length(); k++){
			
				if(k < str[0].length() && k < str[1].length()){
				if(str[0].at(k) == str[1].at(k)){
					continue;
				}
				else{
					
					//str0 prev match
					if(str[0].at(k) == str[0].at(k-1)){
						//delete kth
						//string newstr = str[0].substr(0,k);
						//newstr = newstr + str[0].substr(k+1,(str[0].length()-(k+1));
						//str[0] = newstr;
						//count++;
						
						while(str[0].at(k) != str[1].at(k))
						{
							if(str[0].at(k) == str[0].at(k-1)){
							//delete kth
							string newstr = str[0].substr(0,k);
							newstr = newstr + str[0].substr(k+1,(str[0].length()-(k+1)));
							str[0] = newstr;
							count++;
							
							}
							else{
								
								count = -1;
								cout<<"Case #"<<(i+1)<<": Fegla Won\n";
								break;	
							}
						
						}
					}
					//str1 prev match
					else if(str[1].at(k) == str[1].at(k-1)){
						
						while(str[1].at(k) != str[0].at(k))
						{
							if(str[1].at(k) == str[1].at(k-1)){
							//delete kth
							string newstr = str[1].substr(0,k);
							newstr = newstr + str[1].substr(k+1,(str[1].length()-(k+1)));
							str[1] = newstr;
							count++;
							
							}
							else{
								
								count = -1;
								cout<<"Case #"<<(i+1)<<": Fegla Won\n";
								break;	
							}
						
						}
					}
					else{
						count = -1;
						cout<<"Case #"<<(i+1)<<": Fegla Won\n";
						break;
					}
					
					
				}
			}	
					
				if(k < str[0].length() && k >= str[1].length()){
						//str[1] exhausted!
						while(k < str[0].length())
						{
							if(str[0].at(k) == str[0].at(k-1)){
							//delete kth
							string newstr = str[0].substr(0,k);
							newstr = newstr + str[0].substr(k+1,(str[0].length()-(k+1)));
							str[0] = newstr;
							count++;
							
							}
							else{
								
								count = -1;
								cout<<"Case #"<<(i+1)<<": Fegla Won\n";
								break;	
							}
						
						}	
					}
					if(k >= str[0].length() && k < str[1].length()){
						//str[0] exhausted
						while(k < str[1].length())
						{
							if(str[1].at(k) == str[1].at(k-1)){
							//delete kth
							string newstr = str[1].substr(0,k);
							newstr = newstr + str[1].substr(k+1,(str[0].length()-(k+1)));
							str[1] = newstr;
							count++;
							
							}
							else{
								
								count = -1;
								cout<<"Case #"<<(i+1)<<": Fegla Won\n";
								break;	
							}
						
						}
						
					}
				
				
				if(count == -1){
					break;
				}
				
				}
			
			
			
			
		}

		if(count != -1)
		cout<<"Case #"<<(i+1)<<": "<<count<<"\n";	
			
		
	}
	return 0;
	
}

