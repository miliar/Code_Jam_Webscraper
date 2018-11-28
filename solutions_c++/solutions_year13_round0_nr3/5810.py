bool isPalindrome(int number)
{
	//Convert to string
	string Result;
	ostringstream convert;
	convert << number;
	Result = convert.str();

	if(Result.length() == 1)
	{
		return true;
	}

	string reversed(Result.c_str());
	reverse(reversed.begin(),reversed.end());

	if(Result.compare(reversed) == 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}