#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
	fstream file;
	file.open(argv[1]);
	if(file.is_open())
	{
		int test_count = 0;
		file>>test_count;

		for(int test_id = 1; test_id <= test_count; test_id++)
		{
			bool bcancut_lawn = true;
			int cols = 0;
			int rows = 0;
			file>>rows;
			file>>cols;

			int pattern[100][100] = {0};
			int hmax[100] = {0};
			int vmax[100] = {0};

			for(int i = 0; i < rows; i++)
			{
				for(int j = 0; j < cols; j++)
				{
					int height = 0;
					file >> height;
					pattern[i][j] = height;

					if(height > vmax[j])
					{
						vmax[j] = height;
					}

					if(height > hmax[i])
					{
						hmax[i] = height;
					}
				}
			}

			for(int i = 0; i < rows; i++)
			{
				for(int j = 0; j < cols; j++)
				{
					int height = pattern[i][j];

					if(height != hmax[i] && height != vmax[j])
					{
						bcancut_lawn = false;
						break;
					}
					else if(height == hmax[i])
					{
						// height is in horizontal row..
						// vertical col should be at greater height
						if(vmax[j] < height)
						{
							bcancut_lawn = false;
							break;
						}
					}
					else
					{
						if(hmax[i] < height)
						{
							bcancut_lawn = false;
							break;
						}
					}
				}

				if(!bcancut_lawn)
					break;
			}

			printf("Case #%d: %s\n", test_id, bcancut_lawn? "YES": "NO");
		}
		file.close();
	}
}
