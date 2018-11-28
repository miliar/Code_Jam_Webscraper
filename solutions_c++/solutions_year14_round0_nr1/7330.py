#include <iostream>
#include <string>

using namespace std;
int main()
  {
  	const int N = 4;
	int arr1[N][N];
    int arr2[N][N];
	int T ;
    cin >> T;
  	for (int k = 0; k < T; k++)
      {
      int ans1, ans2;
      cin >> ans1;
      ans1--;
      string answer = "";
      int counter = 0;
      for (int i = 0; i < N; i++)
      	{
      	for (int j = 0; j < N; j++)
        	{
      		cin >> arr1[i][j];
        
	  	}
	  }
      cin >> ans2;
      ans2--;
      for (int i = 0; i < N; i++)
      	{
      	for (int j = 0; j < N; j++)
        	{
      		cin >> arr2[i][j];
        
	  	}
	  }
      for (int i = 0; i < N; i++)
        {
        
        for (int j = 0; j < N; j++)
          {
          
          if (arr1[ans1][i] == arr2[ans2][j])
            {
            counter++;
            answer = to_string(arr1[ans1][i]);
          }
        }
        
        
      }
      if (counter == 0)
        {
        cout << "Case #"<< k+1 <<": Volunteer Cheated!\n";


        
        
    	
      }
      else if (counter == 1)
        {
        
        cout << "Case #"<< k+1 <<": "<<answer<<"\n";


      }
      else if (counter > 1)
        {
        cout << "Case #"<< k+1 <<": Bad Magician!\n";

      }


    } 
}
