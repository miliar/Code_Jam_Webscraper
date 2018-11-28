#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int no_of_cases, t, i, times;
    int num, remainder, answer,temp_num;
    
    int * digit = new int[10];
    
    for (i = 0; i < 10; i++)
		digit[i] = 0; //set 0-9 as 0    	
    
    int finish = 0;
    
	
	cin >> no_of_cases;
    
    
	for (t = 1; t <= no_of_cases; t++) {
        cin >> num ;
        
        for (i = 0; i < 10; i++)
		digit[i] = 0; //set 0-9 as 0   
		
		temp_num = num;
        times = 1;
        finish = 0;
        
        if (num!=0)
        {

        while (finish != 1) {
        	
			temp_num = num * times;
			answer = num * times;
			//cout << "answer is " << answer << endl;
        	while ((temp_num/10) != 0 )
        	{
        		digit[temp_num%10]=1;
        		//cout << "set digit " << temp_num%10 << " = 1" << endl; 
        		temp_num = temp_num / 10;
        		
			}
			digit[temp_num]=1;
			//cout << "set digit " << temp_num << " = 1" << endl; 
			finish = 1;
			for (i = 0; i <10; i++) {
				if (digit[i] == 0 )
					finish = 0;
			}
			times++;
		
        } //finish checking

        cout << "Case #" << t << ": " << answer << endl;
    	}
    	else cout << "Case #" << t << ": " << "INSOMNIA" << endl;
    }
    
    return 0;
}

