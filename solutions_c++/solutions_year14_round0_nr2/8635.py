#include <iostream>
#include <vector>

using namespace std;

class Game
{
	private:
	public:
	double m_cookie_production_target;
	double m_farm_cost; 
	double m_farm_production_rate;

	double m_current_production_rate;
	double m_current_finish_time;
	double m_current_time_remaining;
	double m_current_cookie_count;
	double m_current_elapsed_time;

	Game(double arg_C, double arg_F, double arg_X)
	{
		m_cookie_production_target = arg_X;
		m_farm_cost = arg_C;
		m_farm_production_rate = arg_F;
		
		m_current_production_rate = 2.0000000;
		m_current_cookie_count = 0.0000000;
		m_current_elapsed_time = 0.0000000;
		
		m_current_finish_time = m_cookie_production_target / m_current_production_rate;
		m_current_time_remaining = m_current_finish_time;
		
		
	}
	//------------------------------------------------------------
	double runGame()
	{
		while(true)
		{
			if( m_current_cookie_count >= m_cookie_production_target )
			{
				break;
			}
			
			if( shouldbuyFarm() && canBuyFarm() )
			{
				buyFarm();
			}
			
			makeCookies();
		}
		finishGame();
		
		return m_current_elapsed_time;
		
	}
	//------------------------------------------------------------
	bool canBuyFarm()
	{
		if( m_current_cookie_count >= m_farm_cost )
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	//------------------------------------------------------------

	bool shouldbuyFarm()
	{
		if( getFarmETA() > m_current_time_remaining )
		{
			// Target Cookies produced before farm requirement met 
			return false;
		}
		
		double t_new_time_remaining = getFarmETA() + ( m_cookie_production_target / ( m_current_production_rate + m_farm_production_rate ) );
		
		if( m_current_time_remaining < t_new_time_remaining )
		{
			// Faster to continue without farm than build and restart
			return false;
		}
		
		//----- Optimization: skip to next farm purchase.....
		m_current_elapsed_time += getFarmETA();
		m_current_time_remaining -= m_current_elapsed_time;
		m_current_cookie_count = m_farm_cost;
		
		
		return true;
	}
	
	//------------------------------------------------------------
	void buyFarm()
	{
		m_current_cookie_count = 0.0;
		m_current_production_rate += m_farm_production_rate;
		m_current_time_remaining = m_cookie_production_target / m_current_production_rate;
		
	}
	//------------------------------------------------------------
	void makeCookies( )
	{
		double l_increment = 0.01;
		m_current_cookie_count += l_increment;
		double t_one_cookie_time = ( l_increment / m_current_production_rate );
		m_current_elapsed_time += t_one_cookie_time;
		m_current_time_remaining = m_current_time_remaining - t_one_cookie_time;
		
		
	}
	//------------------------------------------------------------
	double getFarmETA()
	{
		if( m_current_cookie_count > m_farm_cost )
		{
			return 0.0;
		}
		else
		{
			return ( ( m_farm_cost - m_current_cookie_count) / m_current_production_rate  );
		}
		
	}	
	//------------------------------------------------------------
	void finishGame()
	{
		double l_remaining_cookie = m_cookie_production_target - m_current_cookie_count;
		
		m_current_elapsed_time += l_remaining_cookie / m_current_production_rate;
		m_current_cookie_count += l_remaining_cookie;
		m_current_time_remaining = l_remaining_cookie / m_current_production_rate;
	}
		
		
};
	
int main()
{
	int m_test_case_count=0;
	//Get test cases
	cin>>m_test_case_count;
	
	vector<Game> m_game_cases;
	
	double m_C = 0.0, m_F = 0.0, m_X = 0.0;
	
	for( int i = 1; i <= m_test_case_count; i++)
	{
		cin>>m_C;
		cin>>m_F;
		cin>>m_X;
		Game temp_game( m_C, m_F, m_X );
		m_game_cases.push_back(temp_game);
	}
	for( int i = 1; i<=m_test_case_count; i++)
	{
		cout.setf( ios::fixed, ios::floatfield);
		cout.precision(7);
		cout<<"Case #"<<i<<":"<<" "<<m_game_cases.at(i-1).runGame();
		cout<<endl;
	}
	cout<<endl;
	return 0;
}
	
