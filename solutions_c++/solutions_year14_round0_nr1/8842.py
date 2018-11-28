#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;



int main()
{
   const int ROW_NUM = 4;
   const int COL_NUM = 4;

   int test_num;

   cin >> test_num;

   //cout << test_num << endl;

   for (auto i=0; i<test_num; ++i)
   {
	   int ans1, ans2;
	   vector<int> row1;
	   vector<int> row2;

	   cin >> ans1;

           //cout << ans1 << endl;

	   for (auto r=0; r<ROW_NUM; ++r)
	   {
		for (auto c=0; c<COL_NUM; ++c)
		{
			int val;
			cin >> val;
			//cout << val << " ";

			if (r == ans1 - 1)
			   row1.push_back(val);
		}
		//cout << endl;
		  
	   }

	   cin >> ans2; 
	   
 	   //cout << ans2 << endl;
	   for (auto r=0; r<ROW_NUM; ++r)
	   {
		for (auto c=0; c<COL_NUM; ++c)
		{
			int val;
			cin >> val;
			//cout << val << " ";

			if (r == ans2 - 1)
			   row2.push_back(val);
		}	  
		//cout << endl;
	   }

	   sort(row1.begin(), row1.end());
	   sort(row2.begin(), row2.end());

	   vector<int> result;

	   set_intersection(row1.begin(), row1.end(), row2.begin(), row2.end(), std::back_inserter(result));

	   string answer;	
	   if (result.size() == 0)
           {
		answer="Volunteer cheated!";
	   }
	   else if (result.size() > 1)
           {
		answer="Bad magician!";
	   }
	   else
           {
		answer=to_string(result[0]);
           }
	   
	   cout << "Case #" << i+1 <<": " << answer << endl;
    }

   
   
}
