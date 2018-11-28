#include <iostream>
#include <vector>

using namespace std;

class MagicTrick
{
	private:
		int m_deck_size;
		int m_row_size;
		
		int m_row_selected_original;
		int m_row_selected_shuffeled;
	public:
		int m_original_deck[16];
		int m_shuffeled_deck[16];
	
		MagicTrick()
		{
			m_deck_size = 16;
			m_row_size = 4;
		}
		
		void readOriginal()
		{
			cin>>m_row_selected_original;
			for( int i=0; i < m_deck_size; i++)
			{
				cin>>m_original_deck[i];
			}
		}
		
		void readShuffeled()
		{
			cin>>m_row_selected_shuffeled;
			for( int i=0; i < m_deck_size; i++)
			{
				cin>>m_shuffeled_deck[i];
			}
		}
		
		int getRowStartIndex( int  arg_row_num)
		{
			return ( ( arg_row_num - 1 ) * m_row_size );
		}
		
		void evaluateTrick()
		{
			int t_original_start_index = getRowStartIndex( m_row_selected_original );
			int t_shuffeled_start_index = getRowStartIndex( m_row_selected_shuffeled );
			
			int t_match_count = 0;
			int t_match_card=0;
			
			for( int i=t_original_start_index; i< (t_original_start_index + m_row_size); i++ )
			{
				for( int j=t_shuffeled_start_index; j < (t_shuffeled_start_index + m_row_size); j++ )
				{
					if( m_original_deck[i] == m_shuffeled_deck[j] )
					{
						t_match_count++;
						t_match_card = m_original_deck[i];
					}
				}
			}
			
			if( t_match_count == 0 )
			{
				cout<<"Volunteer cheated!";
			}
			if( t_match_count == 1 )
			{
				cout<<t_match_card;
			}
			if( t_match_count > 1)
			{
				cout<<"Bad magician!";
			}
		}
};


int main(int argc, char **argv) 
{
	int m_test_case_count;
	
	//Input number of test cases
	cin>>m_test_case_count;
	
	vector<MagicTrick> m_trick_cases; 
	
	for( int i=1; i<= m_test_case_count; i++ )
	{
		MagicTrick temp_trick;
		temp_trick.readOriginal();
		temp_trick.readShuffeled();
		
		m_trick_cases.push_back(temp_trick);
	}
	for( int i=1; i<= m_test_case_count; i++ )
	{
		cout<<"Case #"<<i<<":"<<" ";
		m_trick_cases.at( i-1 ).evaluateTrick();
		cout<<endl;		
	}
	
	return 0;
}
